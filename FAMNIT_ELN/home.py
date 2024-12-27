from django.shortcuts import render, redirect
from django.apps import apps
from django.contrib.auth import login 
from users.forms import LoginForm
from users.models import CustomUser
from samples.models import Sample, Species, SampleProvider
import json

def home(request):
    if not request.user.is_authenticated:
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
    else:
        form = None
        species_labels = []
        species_data = []
        species = {
            "label": [],
            "data": []
        }
        qs = Species.objects.all()
        for species in qs:
            species_labels.append(species.scientific_name)
            species_data.append(Sample.objects.filter(species=species).count())

        providers_labels = []
        providers_data = []
        providers = SampleProvider.objects.all()
        for provider in providers:
            providers_labels.append(provider.name)
            providers_data.append(Sample.objects.filter(sample_provider=provider).count())
        
        context = {
            'form': form,
            'species_labels': json.dumps(species_labels),
            'species_data': json.dumps(species_data),
            'providers_labels': json.dumps(providers_labels),
            'providers_data': json.dumps(providers_data),
        }
    return render(request, "index.html", context=context)
