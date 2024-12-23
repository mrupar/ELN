from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Sample, Species
from .tables import SampleTable, SpeciesTable
from .forms import SampleForm, SpeciesForm
from datetime import timezone

def samples(request):
    table = SampleTable(Sample.objects.all())
    return render(request, 'samples/samples.html', {'table': table})

def add_sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.instance.date_created = timezone.now()
            form.save()
            messages.success(request, "Sample successfully added!")
            return redirect("/")
    else:
        form = SampleForm()
    return render(request, 'samples/add_sample.html', {'form': form})

def species(request):
    table = SpeciesTable(Species.objects.all())
    return render(request, 'samples/species.html', {'table': table})

def add_species(request):
    if request.method == 'POST':
        form = SpeciesForm(request.POST)
        if form.is_valid():
            form.instance.added_by = request.user
            form.instance.date_created = timezone.now()
            form.save()
            messages.success(request, "Species successfully added!")
            return redirect("/")
    else:
        form = SpeciesForm()
    return render(request, 'samples/add_species.html', {'form': form})