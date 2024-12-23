from django import forms
from .models import Sample
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit 

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        exclude = ['created_by', 'date_created', 'modified_by', 'modified_at', 'uid']

    def __init__(self, *args, **kwargs):
        super(SampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Add Sample'))