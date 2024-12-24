import django_tables2 as tables
from .models import Sample, Species

class SampleTable(tables.Table):
    uid = tables.TemplateColumn(
        '<a href="{% url "edit_samples" record.id %}">{{ record.uid }}</a>',
        verbose_name='UID'
    )

    class Meta:
        model = Sample
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("uid", "name", "species", "sample_provider", "project", "date_created")

class SpeciesTable(tables.Table):
    scientific_name = tables.TemplateColumn(
        '<a href="{% url "edit_species" record.id %}">{{ record.scientific_name }}</a>',
        verbose_name='Scientific Name'
    )
    samples = tables.Column(accessor='sample_set.count', verbose_name='Samples')

    class Meta:
        model = Species
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("scientific_name", "genus", "family", "order", "common_name", "subspecies")