from .models import Thread
import django_tables2 as tables

class ThreadsTable(tables.Table): 
    title = tables.TemplateColumn(
        '<a href="{% url "posts" record.id  %}" data-toggle="tooltip" data-placement="top" title="View Posts">{{ record.title }}</a>'
    )
    delete_checkbox = tables.TemplateColumn(
        '<input type="checkbox" name="threads_to_delete" value="{{ record.id }}" class="delete-checkbox">',
        orderable=False,
        verbose_name='Delete'
    )

    class Meta:
        model = Thread
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("title", "description", "author", "created_at", "delete_checkbox")