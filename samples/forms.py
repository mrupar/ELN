from django import forms
from .models import Sample, Species
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        exclude = ['created_by', 'date_created', 'modified_by', 'modified_at', 'uid']
        widgets = {
            'collection_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'number_of_samples': forms.NumberInput(attrs={'min': 1}),
        }

    def __init__(self, *args, **kwargs):
        super(SampleForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Add Sample'))
        self.helper.add_input(
                Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back()")
            )

        if self.instance and self.instance.pk:
            self.helper.add_input(
                Submit('delete', 'Delete', css_class='btn btn-danger')
            )

class SpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        exclude = ['added_by', 'date_created']
    
    def __init__(self, *args, **kwargs):
        super(SpeciesForm, self).__init__(*args, **kwargs)  
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(
                Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back()")
            )

        if self.instance and self.instance.pk:
            self.helper.add_input(
                Submit('delete', 'Delete', css_class='btn btn-danger')
            )
            