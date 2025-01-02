import django_tables2 as tables
from .models import CustomUser
from django.utils.html import format_html

class UserTable(tables.Table):
    username = tables.TemplateColumn(
        '''
        <a href="{% url "edit_user" record.id %}" data-toggle="tooltip" data-placement="top" title="Edit user">{{ record.username }}</a>
        <a href="{% url "user_history" record.id %}" class="ms-2" data-toggle="tooltip" data-placement="top" title="View history">
            {% load bootstrap_icons %}
            {% bs_icon 'clock-history' %}
        </a>
        ''',
        verbose_name='username'
    )
    date_joined = tables.DateTimeColumn(verbose_name="Date Joined", format="d.m.Y H:i")

    class Meta:
        model = CustomUser
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("username", "email", "first_name", "last_name", "is_active", "is_staff", "is_superuser", "date_joined")

class UserHistoryTable(tables.Table):
    history_date = tables.DateTimeColumn(verbose_name="Date", format="d.m.Y H:i")
    history_user = tables.Column(verbose_name="Modified By")
    history_type = tables.Column(verbose_name="Change Type", accessor="get_history_type_display")
    changes = tables.Column(empty_values=(), verbose_name="Changes")

    class Meta:
        model = CustomUser.history.model
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