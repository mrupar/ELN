import django_tables2 as tables
from .models import Sample

class SampleTable(tables.Table):
    #species = tables.Column(linkify=True)  # Make species clickable
    #sample_provider = tables.Column(linkify=True)  # Make sample provider clickable
    #project = tables.Column(linkify=True)  # Make project clickable

    class Meta:
        model = Sample
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "uid", "species", "sample_provider", "project", "date_created")
