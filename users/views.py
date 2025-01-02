from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileForm, AddUserForm, EditUserForm
from .tables import UserTable, UserHistoryTable
from .filters import UserFilter
from .models import CustomUser

@login_required
def logout_view(request):
    logout(request)
    return redirect("/") # Redirect to the home page (URL name)

@login_required
def profile_view(request):
    user = request.user  # The currently logged-in user
    form = ProfileForm(instance=user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User successfully updated!")
            return redirect("/")

        # Handle password change
        if 'password_change_form' in request.POST:
            current_password = request.POST.get("current_password")
            new_password = request.POST.get("new_password")
            confirm_password = request.POST.get("confirm_password")

            # Check if the current password is correct
            if not user.check_password(current_password):
                messages.error(request, "Current password is incorrect.")
                return redirect("profile")

            # Check if the new password and confirm password match
            if new_password != confirm_password:
                messages.error(request, "New passwords do not match.")
                return redirect("profile")

            # Set the new password
            user.set_password(new_password)
            user.save()

            # Log the user back in with the new password
            update_session_auth_hash(request, user)  # Keeps the user logged in after password change
            messages.success(request, "Your password has been updated successfully.")
            return redirect("profile")

    return render(request, "users/profile.html", {
        "user": user,
        "form": form,
    })


@login_required
@staff_member_required
def users_view(request):
    filter = UserFilter(request.GET, queryset=CustomUser.objects.all())
    table = UserTable(filter.qs)
    return render(request, "users/users.html", {'table': table, 'filter': filter})

@login_required
@staff_member_required
def add_user(request):
    form = AddUserForm()
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            try:
                # Use the create_user method from CustomUserManager
                CustomUser.objects.create_user(
                    email=form.cleaned_data["email"],
                    password="password123",  # Replace this with a secure, dynamic password generation
                    first_name=form.cleaned_data["first_name"],
                    last_name=form.cleaned_data["last_name"],
                    is_staff=form.cleaned_data["is_staff"]
                )
                messages.success(request, "User successfully created!")
                return redirect("/")
            except Exception as e:
                # Handle exceptions like duplicate email or username
                messages.error(request, f"Error creating user: {str(e)}")
        else:
            messages.error(request, "Invalid form submission.")
    return render(request, "users/add_edit_user.html", {"form": form})

@login_required
@staff_member_required
def edit_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    form = EditUserForm(instance=user)
    if request.method == "POST":
        if 'delete' in request.POST:
            if user:
                user.delete()
                messages.success(request, "User deleted successfully!")
                return redirect('users')
        else:
            form = EditUserForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "User successfully added!")
                return redirect("users")
    return render(request, "users/add_edit_user.html", {"form": form, "pk": pk})

def user_history(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    history_records = user.history.all().order_by("-history_date")
    table = UserHistoryTable(history_records)

    return render(request, "history.html", {
        "name": user.username,
        "instance": user,
        "table": table,
    })