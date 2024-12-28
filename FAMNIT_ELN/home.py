from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from users.forms import LoginForm
from users.models import CustomUser
from samples.models import Sample, Species, SampleProvider, Project
from users.models import CustomUser
import json

def login_user_form(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = CustomUser.objects.filter(username=username).first()
            if user:
                if user.check_password(password):
                    login(request, user)  # Log the user in
                    return redirect("/")  # Redirect to the home page
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return form


def home(request):
    context = {
        'total_samples': Sample.objects.count(),
        'total_species': Species.objects.count(),
        'total_providers': SampleProvider.objects.count(),
        'total_projects': Project.objects.count(),
        'total_users': CustomUser.objects.count(),
    }
    
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = login_user_form(request)
            if isinstance(form, HttpResponseRedirect):
                return form
        else:
            form = LoginForm()  
        context.update({"form": form})
    
    # Prepare data for visualization for authenticated users
    species_labels = []
    species_data = []
    species = Species.objects.all()
    for s in species:
        species_labels.append(s.scientific_name)
        species_data.append(Sample.objects.filter(species=s).count())
    
    context.update({
        "species_labels": json.dumps(species_labels),
        "species_data": species_data,
    })
    
    providers_labels = []
    providers_data = []
    providers = SampleProvider.objects.all()
    for provider in providers:
        providers_labels.append(provider.name)
        providers_data.append(Sample.objects.filter(sample_provider=provider).count())
    
    context.update({
        "providers_labels": json.dumps(providers_labels),
        "providers_data": providers_data,
    })

    projects = Project.objects.all()
    projects_labels = ['Active', 'Inactive']
    projects_data = [Project.objects.filter(active=True).count(), 
                     Project.objects.filter(active=False).count()]
    context.update({
        "projects_labels": json.dumps(projects_labels),
        "projects_data": projects_data,
    })
    
    return render(request, "index.html", context=context)
