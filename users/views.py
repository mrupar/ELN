from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Hash password
            user.save()
            login(request, user)  # Log the user in immediately after signup
            return redirect("/")  # Redirect to the home page
    else:
        form = SignupForm()
    
    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)  # Authenticate the user
            if user is not None:
                login(request, user)  # Log the user in
                return redirect("/")  # Redirect to the home page
            else:
                form.add_error(None, "Invalid username or password.")  # Add an error to the form
    else:
        form = LoginForm()
    
    return render(request, "users/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return redirect("/") # Redirect to the home page (URL name)

@login_required
def profile_view(request):
    user = request.user  # The currently logged-in user
    return render(request, "users/profile.html", {"user": user})