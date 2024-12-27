from dal import autocomplete
from django import forms
from django_countries.fields import CountryField
from .models import Sample, Species, Project, SampleProvider
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        exclude = ['uid']
        widgets = {
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
        fields = ('__all__')
    
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
            
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('__all__')
    
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)  
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(
                Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back()")
            )

        if self.instance and self.instance.pk:
            self.helper.add_input(
                Submit('delete', 'Delete', css_class='btn btn-danger')
            )

class SampleProviderForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}))
    country = forms.ChoiceField(
        widget=autocomplete.ListSelect2(url='country-autocomplete'),
    )

    class Meta:
        model = SampleProvider
        fields = ('__all__')
    
    def __init__(self, *args, **kwargs):
        super(SampleProviderForm, self).__init__(*args, **kwargs)  
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(
                Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back()")
            )

        if self.instance and self.instance.pk:
            self.helper.add_input(
                Submit('delete', 'Delete', css_class='btn btn-danger')
            )