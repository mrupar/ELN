from django import forms
from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter
from .models import Sample, Species, Project, SampleProvider
from dal import autocomplete

class SampleFilter(FilterSet):
    uid = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'UID',
            'class': 'form-control',
        })
    )
    name = CharFilter(
        lookup_expr='icontains',
        label='Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': 'form-control',
                }
            )
        )
    species = ModelMultipleChoiceFilter(
        queryset=Species.objects.all(),
        label='',
        widget=autocomplete.ModelSelect2Multiple(
            url='species-autocomplete',
            attrs={
                'data-placeholder': 'Species',
                'class': 'form-control',
                }
            )
        )
    project = ModelMultipleChoiceFilter(
        queryset=Project.objects.all(),
        label='',
        widget=autocomplete.ModelSelect2Multiple(
            url='project-autocomplete',
            attrs={
                'data-placeholder': 'Projects',
                'class': 'form-control',
                }
            )
        )
    sample_provider = ModelMultipleChoiceFilter(
        queryset=SampleProvider.objects.all(),
        label='',
        widget=autocomplete.ModelSelect2Multiple(
            url='sample-provider-autocomplete',
            attrs={
                'data-placeholder': 'Sample Providers',
                'class': 'form-control',
                }
            )
        )

    class Meta:
        model = Sample
        fields = [
            'uid', 
            'name', 
            'species', 
            'project', 
            'sample_provider'
            ]


class SpeciesFilter(FilterSet):
    scientific_name = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Scientific Name',
            'class': 'form-control',
        })
    )
    genus = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Genus',
            'class': 'form-control',
        })
    )
    family = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Family',
            'class': 'form-control',
        })
    )
    order = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Order',
            'class': 'form-control',
        })
    )
    common_name = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Common Name',
            'class': 'form-control',
        })
    )
    subspecies = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Subspecies',
            'class': 'form-control',
        })
    )

    class Meta:
        model = Species
        fields = [
            'scientific_name',
            'genus',
            'family',
            'order',
            'common_name',
            'subspecies',
        ]
