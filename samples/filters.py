from django import forms
from django_filters import FilterSet, filters, CharFilter
from django.db.models import Q
from .models import Sample

class SampleFilter(FilterSet):
    query = CharFilter(
        method='universal_search',
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Search...'})
        )
    
    class Meta:
        model = Sample
        fields = ['query']

    def universal_search(self, queryset, name, value):
        return Sample.objects.filter(
            Q(uid__icontains=value) |
            Q(species__scientific_name__icontains=value) | 
            Q(project__name__icontains=value) |
            Q(name__icontains=value) |
            Q(sample_provider__name__icontains=value)
        )
