from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Sample, Species, Project, SampleProvider
from .tables import SampleTable, SpeciesTable, ProjectTable, SampleProviderTable, \
    ProjectHistoryTable, SampleHistoryTable, SpeciesHistoryTable, SampleProviderHistoryTable
from .forms import SampleForm, SpeciesForm, ProjectForm, SampleProviderForm
from .filters import SampleFilter, SpeciesFilter, ProjectFilter, SampleProviderFilter

def add_edit_instance(request, form, instance, redirect_url, type, action):
    if request.method == 'POST':
        if 'delete' in request.POST:
            if instance:
                instance.delete()
                messages.success(request, f"{type} deleted successfully!")
                return redirect(redirect_url)
        else:
            form = form(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                messages.success(request, f"{type} {action} successfully!")
                return redirect(redirect_url)
    else:
        form = form(instance=instance)
    return render(request, 'add_edit_instance.html', {
        'form': form, 
        'instance': instance, 
        'type': type
        })

# SAMPLES
def samples(request):
    filter = SampleFilter(request.GET, queryset=Sample.objects.all())
    table = SampleTable(filter.qs)
    return render(request, 'samples/samples.html', {'table': table, 'filter': filter})

def add_edit_sample(request, pk=None):
    sample = get_object_or_404(Sample, pk=pk) if pk else None
    action = 'edited' if pk else 'added'
    return add_edit_instance(
        request=request,
        form=SampleForm,
        instance=sample,
        redirect_url='samples',
        type='Sample',
        action=action
        )

def sample_history(request, pk):
    sample = get_object_or_404(Sample, pk=pk)
    history_records = sample.history.all().order_by("-history_date")
    table = SampleHistoryTable(history_records)

    return render(request, "history.html", {
        'name': f'Sample {sample.name}: {sample.uid}',
        "instance": sample,
        "table": table,
    })

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
    action = 'edited' if pk else 'added'
    return add_edit_instance(
        request=request,
        form=SpeciesForm,
        instance=species,
        redirect_url='species',
        type='Species',
        action=action
        )

def species_history(request, pk):
    species = get_object_or_404(Species, pk=pk)
    history_records = species.history.all().order_by("-history_date")
    table = SpeciesHistoryTable(history_records)

    return render(request, "history.html", {
        "name": species.scientific_name,
        "instance": species,
        "table": table,
    })

#------------------------------------------------------------

# PROJECTS
def projects(request):
    filter = ProjectFilter(request.GET, queryset=Project.objects.all())
    table = ProjectTable(filter.qs)
    return render(request, 'samples/projects.html', {'table': table, 'filter': filter})

def add_edit_project(request, pk=None):
    project = get_object_or_404(Project, pk=pk) if pk else None
    action = 'edited' if pk else 'added'
    return add_edit_instance(
        request=request,
        form=ProjectForm,
        instance=project,
        redirect_url='projects',
        type='Project',
        action=action
        )

def project_history(request, pk):
    project = get_object_or_404(Project, pk=pk)
    history_records = project.history.all().order_by("-history_date")
    table = ProjectHistoryTable(history_records)

    return render(request, "history.html", {
        "name": project.name,
        "instance": project,
        "table": table,
    })

#------------------------------------------------------------

# SAMPLE PROVIDER
def sample_provider(request):
    filter = SampleProviderFilter(request.GET, queryset=SampleProvider.objects.all())
    table = SampleProviderTable(filter.qs)
    return render(request, 'samples/sample_provider.html', {'table': table, 'filter': filter})

def add_edit_sample_provider(request, pk=None):
    sample_provider = get_object_or_404(SampleProvider, pk=pk) if pk else None
    action = 'edited' if pk else 'added'
    return add_edit_instance(
        request=request,
        form=SampleProviderForm,
        instance=sample_provider,
        redirect_url='sample_providers',
        type='Sample Provider',
        action=action
        )

def sample_provider_history(request, pk):
    sample_provider = get_object_or_404(SampleProvider, pk=pk)
    history_records = sample_provider.history.all().order_by("-history_date")
    table = SampleProviderHistoryTable(history_records)

    return render(request, "history.html", {
        "name": sample_provider.name,
        "instance": sample_provider,
        "table": table,
    })