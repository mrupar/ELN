from django.shortcuts import render, redirect
from django.apps import apps
from django.contrib.auth import login 
from users.forms import LoginForm
from users.models import CustomUser

def home(request):
    if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]

                user = CustomUser.objects.get(username=username)

                if user.check_password(password):
                    login(request, user)  # Log the user in
                    return redirect("/")  # Redirect to the home page
                else:
                    form.add_error(None, "Invalid username or password.")  # Add an error to the form
    else:
        form = LoginForm()
    return render(request, "index.html", {'form': form})
