import django_tables2 as tables
from django.utils.html import format_html
from .models import Sample, Species, Project, SampleProvider

class SampleTable(tables.Table):
    uid = tables.TemplateColumn(
        '''
        <a href="{% url "edit_samples" record.id %}" data-toggle="tooltip" data-placement="top" title="Edit sample">{{ record.uid }}</a>
        <a href="{% url "sample_history" record.id %}" class="ms-2" data-toggle="tooltip" data-placement="top" title="View history">
            {% load bootstrap_icons %}
            {% bs_icon 'clock-history' %}
        </a>
        ''',
        verbose_name='UID',
        order_by="uid"  # Ensure this matches a field in the model
    )

    class Meta:
        model = Sample
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("uid", "name", "species", "sample_provider", "project")    
        order_by = ["-uid"]

    def order_uid(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "uid")
        return queryset, is_descending

    def order_name(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "name")
        return queryset, is_descending

    def order_species(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "species")
        return queryset, is_descending

    def order_sample_provider(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "sample_provider")
        return queryset, is_descending

    def order_project(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "project")
        return queryset, is_descending


class SpeciesTable(tables.Table):
    scientific_name = tables.TemplateColumn(
        '''
        <a href="{% url "edit_species" record.id %}" data-toggle="tooltip" data-placement="top" title="Edit species">{{ record.scientific_name }}</a>
        <a href="{% url "species_history" record.id %}" class="ms-2" data-toggle="tooltip" data-placement="top" title="View history">
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

    def order_scientific_name(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "scientific_name")
        return queryset, is_descending
    
    def order_genus(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "genus")
        return queryset, is_descending
    
    def order_family(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "family")
        return queryset, is_descending
    
    def order_order(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "order")
        return queryset, is_descending
    
    def order_common_name(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "common_name")
        return queryset, is_descending
    
    def order_subspecies(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "subspecies")
        return queryset, is_descending
    
    def order_samples(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "samples")
        return queryset, is_descending

class ProjectTable(tables.Table):
    name = tables.TemplateColumn(
        '''
        <a href="{% url "edit_project" record.id %}" data-toggle="tooltip" data-placement="top" title="Edit project">{{ record.name }}</a>
        <a href="{% url "project_history" record.id %}" class="ms-2" data-toggle="tooltip" data-placement="top" title="View history">
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

    def order_name(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "name")
        return queryset, is_descending
    
    def order_description(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "description")
        return queryset, is_descending
    
    def order_active(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "active")
        return queryset, is_descending

class SampleProviderTable(tables.Table):
    name = tables.TemplateColumn(
        '''
        <a href="{% url "edit_sample_provider" record.id %}" data-toggle="tooltip" data-placement="top" title="Edit provider">{{ record.name }}</a>
        <a href="{% url "sample_provider_history" record.id %}" class="ms-2" data-toggle="tooltip" data-placement="top" title="View history">
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

    def order_name(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "name")
        return queryset, is_descending
    
    def order_short_name(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "short_name")
        return queryset, is_descending
    
    def order_address(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "address")
        return queryset, is_descending
    
    def order_country(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "country")
        return queryset, is_descending
    
    def order_contact_email(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "contact_email")
        return queryset, is_descending
    
    def order_phone_number(self, queryset, is_descending):
        queryset = queryset.order_by(("-" if is_descending else "") + "phone_number")
        return queryset, is_descending

# History Tables
class ProjectHistoryTable(tables.Table):
    history_date = tables.DateTimeColumn(verbose_name="Date", format="d.m.Y H:i")
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
    history_date = tables.DateTimeColumn(verbose_name="Date", format="d.m.Y H:i")
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
    history_date = tables.DateTimeColumn(verbose_name="Date", format="d.m.Y H:i")
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
    history_date = tables.DateTimeColumn(verbose_name="Date", format="d.m.Y H:i")
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