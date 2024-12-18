from django.shortcuts import render
from .models import Sample
from .tables import SampleTable

def samples(request):
    table = SampleTable(Sample.objects.all())
    return render(request, 'samples/samples.html', {'table': table})

