from django import forms
from .models import Category, Thread, Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(
                Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back()")
            )

        if self.instance and self.instance.pk:
            self.helper.add_input(
                Submit('delete', 'Delete', css_class='btn btn-danger')
            )

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'description'] 

    def __init__(self, *args, **kwargs):
        super(ThreadForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        self.helper.add_input(
                Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back()")
            )
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content'] 

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
