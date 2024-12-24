from django_filters import FilterSet, filters
from .models import Sample
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit, Fieldset

class SampleFilter(FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    species = filters.CharFilter(lookup_expr='scientific_name__icontains')
    project = filters.CharFilter(lookup_expr='name__icontains')
    sample_provider = filters.CharFilter(lookup_expr='name__icontains')
    
    class Meta:
        model = Sample
        fields = ['species', 'project', 'name', 'sample_provider']

    def __init__(self, *args, **kwargs):
        super(SampleFilter, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'  # Ensure form uses GET method
        self.helper.layout = Layout(
            Fieldset(
                'Filter by',
                Row(
                    Column('name', css_class='form-group col-md-3 mb-0'),
                    Column('species', css_class='form-group col-md-3 mb-0'),
                    Column('project', css_class='form-group col-md-3 mb-0'),
                ),
                Row(
                    Column('sample_provider', css_class='form-group col-md-3 mb-0'),
                ),
            ),
            Submit('submit', 'Submit')  # Submit button to apply the filter
        )
