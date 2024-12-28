import django_tables2 as tables
from .models import CustomUser

class UserTable(tables.Table):
    username = tables.TemplateColumn(
        '<a href="{% url "edit_user" record.id %}">{{ record.username }}</a>',
        verbose_name='username'
    )

    class Meta:
        model = CustomUser
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("username", "email", "first_name", "last_name", "is_active", "is_staff", "is_superuser", "date_joined")