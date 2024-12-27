from django import forms
from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter, ChoiceFilter, MultipleChoiceFilter
from django_countries import countries
from .models import Sample, Species, Project, SampleProvider
from dal import autocomplete

class SampleFilter(FilterSet):
    uid = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'UID',
                'class': 'form-control',
                },
            ),
        )
    name = CharFilter(
        lookup_expr='icontains',
        label='Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': 'form-control',
                },
            ),
        )
    species = ModelMultipleChoiceFilter(
        queryset=Species.objects.all(),
        label='',
        widget=autocomplete.ModelSelect2Multiple(
            url='species-autocomplete',
            attrs={
                'data-placeholder': 'Species',
                'class': 'form-control',
                },
            ),
        )
    project = ModelMultipleChoiceFilter(
        queryset=Project.objects.all(),
        label='',
        widget=autocomplete.ModelSelect2Multiple(
            url='project-autocomplete',
            attrs={
                'data-placeholder': 'Projects',
                'class': 'form-control',
                },
            ),
        )
    sample_provider = ModelMultipleChoiceFilter(
        queryset=SampleProvider.objects.all(),
        label='',
        widget=autocomplete.ModelSelect2Multiple(
            url='sample-provider-autocomplete',
            attrs={
                'data-placeholder': 'Sample Providers',
                'class': 'form-control',
                },
            ),
        )
    
    class Meta:
        model = Sample
        fields = [
            'uid', 
            'name', 
            'species', 
            'project', 
            'sample_provider',
            ]

class SpeciesFilter(FilterSet):
    scientific_name = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Scientific Name',
                'class': 'form-control',
                },
            ),
        )
    genus = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Genus',
                'class': 'form-control',
                },
            ),
        )
    family = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Family',
                'class': 'form-control',
                },
            ),
        )
    order = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Order',
                'class': 'form-control',
                },
            ),
        )
    common_name = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Common Name',
                'class': 'form-control',
                },
            ),
        )
    subspecies = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Subspecies',
                'class': 'form-control',
                },
            ),
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

class ProjectFilter(FilterSet):
    name = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': 'form-control',
                },
            ),
        )
    active = ChoiceFilter(
        choices=(
            (True, 'Yes'),
            (False, 'No'),
        ),
        empty_label='All',
        label='',
        widget=forms.Select(
            attrs={'class': 'form-control'},
            )
        )

    class Meta:
        model = Project
        fields = [
            'name',
            'active',
            ]

class SampleProviderFilter(FilterSet):
    name = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'class': 'form-control',
                },
            ),
        )
    short_name = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Short Name',
                'class': 'form-control',
                }, 
            ),
        )
    country = MultipleChoiceFilter(
        choices=countries,
        label='',
        widget=autocomplete.Select2Multiple(
            url='country-autocomplete',
            attrs={
                'data-placeholder': 'Select countries',
                'class': 'form-control',
                },
            ),
        )

    class Meta:
        model = SampleProvider
        fields = [
            'name',
            'short_name',
            'country',
            ]