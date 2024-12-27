from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Sample, Species, Project, SampleProvider
from .tables import SampleTable, SpeciesTable, ProjectTable, SampleProviderTable
from .forms import SampleForm, SpeciesForm, ProjectForm, SampleProviderForm
from .filters import SampleFilter, SpeciesFilter, ProjectFilter, SampleProviderFilter

# SAMPLES
def samples(request):
    filter = SampleFilter(request.GET, queryset=Sample.objects.all())
    table = SampleTable(filter.qs)
    return render(request, 'samples/samples.html', {'table': table, 'filter': filter})

def add_edit_sample(request, pk=None):
    sample = get_object_or_404(Sample, pk=pk) if pk else None
    if request.method == 'POST':
        if 'delete' in request.POST:
            if sample:
                sample.delete()
                messages.success(request, "Sample deleted successfully!")
                return redirect('samples')
        else:
            form = SampleForm(request.POST, instance=sample)
            if form.is_valid():
                form.save()
                messages.success(request, "Sample successfully added!")
                return redirect("samples")
    else:
        form = SampleForm(instance=sample)
    return render(request, 'samples/add_edit_sample.html', {'form': form, 'sample': sample})

#------------------------------------------------------------

# SPECIES
def species(request):
    queryset = Species.objects.all()
    filter = SpeciesFilter(request.GET, queryset=queryset)
    table = SpeciesTable(filter.qs)
    return render(
        request,
        'samples/species.html',
        {'table': table, 'filter': filter}
    )

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
                form.save()
                messages.success(request, f"Species {'updated' if pk else 'added'} successfully!")
                return redirect('species')  # Replace with your actual table view name
    else:
        form = SpeciesForm(instance=species)

    return render(request, 'samples/add_edit_species.html', {'form': form, 'species': species})

#------------------------------------------------------------

# PROJECTS
def projects(request):
    filter = ProjectFilter(request.GET, queryset=Project.objects.all())
    table = ProjectTable(filter.qs)
    return render(request, 'samples/projects.html', {'table': table, 'filter': filter})

def add_edit_project(request, pk=None):
    project = get_object_or_404(Project, pk=pk) if pk else None
    if request.method == 'POST':
        if 'delete' in request.POST:
            if project:
                project.delete()
                messages.success(request, "Project deleted successfully!")
                return redirect('projects')
        else:
            form = ProjectForm(request.POST, instance=project)
            if form.is_valid():
                form.save()
                messages.success(request, "Project successfully added!")
                return redirect("projects")
    else:
        form = ProjectForm(instance=project)
    return render(request, 'samples/add_edit_project.html', {'form': form, 'project': project})

#------------------------------------------------------------

# SAMPLE PROVIDER
def sample_provider(request):
    filter = SampleProviderFilter(request.GET, queryset=SampleProvider.objects.all())
    table = SampleProviderTable(filter.qs)
    return render(request, 'samples/sample_provider.html', {'table': table, 'filter': filter})

def add_edit_sample_provider(request, pk=None):
    sample_provider = get_object_or_404(SampleProvider, pk=pk) if pk else None
    if request.method == 'POST':
        if 'delete' in request.POST:
            if sample_provider:
                sample_provider.delete()
                messages.success(request, "Sample provider deleted successfully!")
                return redirect('sample_providers')
        else:
            form = SampleProviderForm(request.POST, instance=sample_provider)
            if form.is_valid():
                form.save()
                messages.success(request, "Sample provider successfully added!")
                return redirect("sample_providers")
    else:
        form = SampleProviderForm(instance=sample_provider)
    return render(request, 'samples/add_edit_sample_provider.html', {'form': form, 'sample_provider': sample_provider})