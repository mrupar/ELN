import django_tables2 as tables
from .models import Sample, Species, Project, SampleProvider

class SampleTable(tables.Table):
    uid = tables.TemplateColumn(
        '<a href="{% url "edit_samples" record.id %}">{{ record.uid }}</a>',
        verbose_name='UID'
    )

    class Meta:
        model = Sample
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("uid", "name", "species", "sample_provider", "project")

class SpeciesTable(tables.Table):
    scientific_name = tables.TemplateColumn(
        '<a href="{% url "edit_species" record.id %}">{{ record.scientific_name }}</a>',
        verbose_name='Scientific Name'
    )
    samples = tables.TemplateColumn(
        '<a href="{% url "samples" %}?species={{ record.id }}"> Samples of {{ record.scientific_name }}</a>',
        verbose_name='Samples'
    )

    class Meta:
        model = Species
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("scientific_name", "genus", "family", "order", "common_name", "subspecies", "samples")

class ProjectTable(tables.Table):
    name = tables.TemplateColumn(
        '<a href="{% url "edit_project" record.id %}">{{ record.name }}</a>',
        verbose_name='Name'
    )

    class Meta:
        model = Project
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "description", "active")

class SampleProviderTable(tables.Table):
    name = tables.TemplateColumn(
        '<a href="{% url "edit_sample_provider" record.id %}">{{ record.name }}</a>',
        verbose_name='Name'
    )

    class Meta:
        model = SampleProvider
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "short_name", "address", "country", "contact_email", "phone_number")