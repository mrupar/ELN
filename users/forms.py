from django import forms
from .models import CustomUser as User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit 

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your username"}),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter your password"}),
        label="Password"
    )

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Login'))


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["date_joined", "last_login", "is_active", "is_staff", "password"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your first name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your last name"}),
        }

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Update'))

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "is_staff"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your first name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your last name"}),
            "is_staff": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize the FormHelper
        self.helper = FormHelper()
        # Add the submit button
        self.helper.add_input(Submit('submit', 'Add User'))

    def save(self, commit=True):
        user = super(AddUserForm, self).save(commit=False)
        user.set_password("password123")
        if commit:
            user.save()
        return user