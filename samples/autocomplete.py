from dal import autocomplete
from .models import Species, Project, SampleProvider

class SpeciesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Species.objects.all()
        if self.q: 
            qs = qs.filter(scientific_name__icontains=self.q) 

        return qs
    
class ProjectAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):

        qs = Project.objects.all()
        if self.q: 
            qs = qs.filter(name__icontains=self.q)  

        return qs

class SampleProviderAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SampleProvider.objects.all()
        if self.q: 
            qs = qs.filter(name__icontains=self.q)  
        return qs