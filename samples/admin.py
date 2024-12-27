from django.contrib import admin
from .models import Project, SampleProvider, Species, Sample

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(SampleProvider)
class SampleProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'country')
    search_fields = ('name', 'short_name', 'country')
    ordering = ('name',)


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('scientific_name', 'common_name', 'genus', 'family', 'order')
    list_filter = ('genus', 'family', 'order')
    search_fields = ('scientific_name', 'common_name', 'genus', 'family', 'order')
    ordering = ('scientific_name',)


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'species', 'sample_provider', 'project', 'number_of_samples')
    list_filter = ('species', 'sample_provider', 'project')
    search_fields = ('uid', 'name', 'species__scientific_name', 'project__name')

    # Inline editing of related models
    autocomplete_fields = ('species', 'sample_provider')
