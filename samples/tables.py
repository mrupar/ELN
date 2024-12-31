import django_tables2 as tables
from django.utils.html import format_html
from .models import Sample, Species, Project, SampleProvider

class SampleTable(tables.Table):
    uid = tables.TemplateColumn(
        '''
        <a href="{% url "edit_samples" record.id %}">{{ record.uid }}</a>
        <a href="{% url "sample_history" record.id %}" class="ms-2">
            {% load bootstrap_icons %}
            {% bs_icon 'clock-history' %}
        </a>
        ''',
        verbose_name='UID'
    )

    class Meta:
        model = Sample
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("uid", "name", "species", "sample_provider", "project")

class SpeciesTable(tables.Table):
    scientific_name = tables.TemplateColumn(
        '''
        <a href="{% url "edit_species" record.id %}">{{ record.scientific_name }}</a>
        <a href="{% url "species_history" record.id %}" class="ms-2">
            {% load bootstrap_icons %}
            {% bs_icon 'clock-history' %}
        </a>
        ''',
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
        '''
        <a href="{% url "edit_project" record.id %}">{{ record.name }}</a>
        <a href="{% url "project_history" record.id %}" class="ms-2">
            {% load bootstrap_icons %}
            {% bs_icon 'clock-history' %}
        </a>
        ''',
        verbose_name='Name'
    )

    class Meta:
        model = Project
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "description", "active")

class SampleProviderTable(tables.Table):
    name = tables.TemplateColumn(
        '''
        <a href="{% url "edit_sample_provider" record.id %}">{{ record.name }}</a>
        <a href="{% url "sample_provider_history" record.id %}" class="ms-2">
            {% load bootstrap_icons %}
            {% bs_icon 'clock-history' %}
        </a>
        ''',
        verbose_name='Name'
    )

    class Meta:
        model = SampleProvider
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "short_name", "address", "country", "contact_email", "phone_number")

# History Tables
class ProjectHistoryTable(tables.Table):
    history_date = tables.DateTimeColumn(verbose_name="Date")
    history_user = tables.Column(verbose_name="Modified By")
    history_type = tables.Column(verbose_name="Change Type", accessor="get_history_type_display")
    changes = tables.Column(empty_values=(), verbose_name="Changes")

    class Meta:
        model = Project.history.model
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("history_date", "history_user", "history_type")

    def render_changes(self, record):
        if record.prev_record:
            changes = []
            for field in record.instance._meta.fields:
                field_name = field.name
                old_value = getattr(record.prev_record, field_name, None)
                new_value = getattr(record, field_name, None)
                if old_value != new_value:
                    changes.append(f"<strong>{field.verbose_name}:</strong> {old_value} → {new_value}")
            return format_html("<br>".join(changes))
        return "No previous record"
    
class SampleHistoryTable(tables.Table):
    history_date = tables.DateTimeColumn(verbose_name="Date")
    history_user = tables.Column(verbose_name="Modified By")
    history_type = tables.Column(verbose_name="Change Type", accessor="get_history_type_display")
    changes = tables.Column(empty_values=(), verbose_name="Changes")

    class Meta:
        model = Sample.history.model
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("history_date", "history_user", "history_type")

    def render_changes(self, record):
        if record.prev_record:
            changes = []
            for field in record.instance._meta.fields:
                field_name = field.name
                old_value = getattr(record.prev_record, field_name, None)
                new_value = getattr(record, field_name, None)
                if old_value != new_value:
                    changes.append(f"<strong>{field.verbose_name}:</strong> {old_value} → {new_value}")
            return format_html("<br>".join(changes))
        return "No previous record"
    
class SpeciesHistoryTable(tables.Table):
    history_date = tables.DateTimeColumn(verbose_name="Date")
    history_user = tables.Column(verbose_name="Modified By")
    history_type = tables.Column(verbose_name="Change Type", accessor="get_history_type_display")
    changes = tables.Column(empty_values=(), verbose_name="Changes")

    class Meta:
        model = Species.history.model
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("history_date", "history_user", "history_type")

    def render_changes(self, record):
        if record.prev_record:
            changes = []
            for field in record.instance._meta.fields:
                field_name = field.name
                old_value = getattr(record.prev_record, field_name, None)
                new_value = getattr(record, field_name, None)
                if old_value != new_value:
                    changes.append(f"<strong>{field.verbose_name}:</strong> {old_value} → {new_value}")
            return format_html("<br>".join(changes))
        return "No previous record"
    
class SampleProviderHistoryTable(tables.Table):
    history_date = tables.DateTimeColumn(verbose_name="Date")
    history_user = tables.Column(verbose_name="Modified By")
    history_type = tables.Column(verbose_name="Change Type", accessor="get_history_type_display")
    changes = tables.Column(empty_values=(), verbose_name="Changes")

    class Meta:
        model = SampleProvider.history.model
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("history_date", "history_user", "history_type")

    def render_changes(self, record):
        if record.prev_record:
            changes = []
            for field in record.instance._meta.fields:
                field_name = field.name
                old_value = getattr(record.prev_record, field_name, None)
                new_value = getattr(record, field_name, None)
                if old_value != new_value:
                    changes.append(f"<strong>{field.verbose_name}:</strong> {old_value} → {new_value}")
            return format_html("<br>".join(changes))
        return "No previous record"