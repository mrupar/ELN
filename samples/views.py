from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Sample, Species
from .tables import SampleTable, SpeciesTable
from .forms import SampleForm, SpeciesForm

# SAMPLES
def samples(request):
    table = SampleTable(Sample.objects.all())
    return render(request, 'samples/samples.html', {'table': table})

def add_edit_sample(request, pk=None):
    sample = get_object_or_404(Sample, pk=pk) if pk else None
    if request.method == 'POST':
        if 'delete' in request.POST:
            if species:
                species.delete()
                messages.success(request, "Species deleted successfully!")
                return redirect('samples')
        else:
            form = SampleForm(request.POST, instance=sample)
            if form.is_valid():
                form.instance.added_by = request.user
                form.save()
                messages.success(request, "Sample successfully added!")
                return redirect("samples")
    else:
        form = SampleForm(instance=sample)
    return render(request, 'samples/add_sample.html', {'form': form, 'sample': sample})
#------------------------------------------------------------
# SPECIES
def species(request):
    table = SpeciesTable(Species.objects.all())
    return render(request, 'samples/species.html', {'table': table})

def add_edit_species(request, pk=None):
    species = get_object_or_404(Species, pk=pk) if pk else None

    if request.method == 'POST':
        if 'delete' in request.POST:
            if species:
                species.delete()
                messages.success(request, "Species deleted successfully!")
                return redirect('species')
        else:
            form = SpeciesForm(request.POST, instance=species)
            if form.is_valid():
                form.instance.added_by = request.user
                form.save()
                messages.success(request, f"Species {'updated' if pk else 'added'} successfully!")
                return redirect('species')  # Replace with your actual table view name
    else:
        form = SpeciesForm(instance=species)

    return render(request, 'samples/add_species.html', {'form': form, 'species': species})
#------------------------------------------------------------