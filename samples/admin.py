from django.contrib import admin
from .models import Project, SampleProvider, Species, Sample

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by', 'date_created')
    list_filter = ('date_created',)
    search_fields = ('name', 'created_by__username')
    ordering = ('-date_created',)
    readonly_fields = ('date_created', 'modified_by', 'modified_at')


@admin.register(SampleProvider)
class SampleProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'country', 'provided_by', 'date_created')
    list_filter = ('country', 'provided_by')
    search_fields = ('name', 'short_name', 'provided_by__username', 'country')
    ordering = ('name',)
    readonly_fields = ('date_created',)


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('scientific_name', 'common_name', 'genus', 'family', 'order', 'date_created')
    list_filter = ('genus', 'family', 'order')
    search_fields = ('scientific_name', 'common_name', 'genus', 'family', 'order')
    ordering = ('scientific_name',)
    readonly_fields = ('date_created',)


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('uid', 'name', 'species', 'sample_provider', 'project', 'created_by', 'number_of_samples', 'date_created')
    list_filter = ('species', 'sample_provider', 'project', 'date_created')
    search_fields = ('uid', 'name', 'species__scientific_name', 'sample_provider__name', 'project__name', 'created_by__username')
    ordering = ('-date_created',)
    readonly_fields = ('date_created', 'modified_at', 'modified_by')

    # Inline editing of related models
    autocomplete_fields = ('species', 'sample_provider', 'project', 'created_by')
