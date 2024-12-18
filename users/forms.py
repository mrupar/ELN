from django import forms
from .models import CustomUser as User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit 

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["date_joined", "last_login", "is_active", "is_staff"]
        widgets = {
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter your password"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}),
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter your password"}),
        }

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
