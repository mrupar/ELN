from django.shortcuts import render
from .models import Sample
from .tables import SampleTable
from .forms import SampleForm

def samples(request):
    table = SampleTable(Sample.objects.all())
    return render(request, 'samples/samples.html', {'table': table})

def add_sample(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SampleForm()
    return render(request, 'samples/add_sample.html', {'form': form})
