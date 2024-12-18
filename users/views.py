from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Hash password
            user.save()
            return redirect("users/login")  # Redirect to the login page (URL name)
    else:
        form = SignupForm()
    
    return render(request, "users/signup.html", {"form": form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Hash password
            user.save()
            return redirect("users/login")  # Redirect to the login page (URL name)
    else:
        form = LoginForm()
    
    return render(request, "users/login.html", {"form": form})