from .models import Thread
import django_tables2 as tables
from django.utils.html import format_html

class ThreadsTable(tables.Table): 
    title = tables.TemplateColumn(
        '<a href="{% url "posts" record.id  %}" data-toggle="tooltip" data-placement="top" title="View Posts">{{ record.title }}</a>'
    )
    delete_checkbox = tables.TemplateColumn(
        '<input type="checkbox" name="threads_to_delete" value="{{ record.id }}" class="delete-checkbox">',
        orderable=False,
        verbose_name=format_html(
            '''
            <div>
                <label for="select_all_checkbox" class="mb-0 mr-2" title="Select All">Delete</label>
                <input type="checkbox" name="select_all" class="checkbox" title="Select All" id="select_all_checkbox">
            </div>
            '''
        )
    )

    class Meta:
        model = Thread
        attrs = {"class": "table table-striped table-hover table-bordered shadow-sm"}
        template_name = "django_tables2/bootstrap4.html"
        fields = ("title", "description", "author", "created_at", "delete_checkbox")