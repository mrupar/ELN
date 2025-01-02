from django import forms
from .models import CustomUser as User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button

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
        exclude = ["date_joined", "last_login", "is_active", "is_superuser", "is_staff", "password", "groups", "user_permissions"]
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
    
class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "is_active", "is_staff", "is_superuser"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}),
            "first_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your first name"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your last name"}),
            "is_staff": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "is_active": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "is_superuser": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Initialize the FormHelper
        self.helper = FormHelper()
        # Add the submit button
        self.helper.add_input(Submit('submit', 'Update User'))

        self.helper.add_input(
                Button('cancel', 'Cancel', css_class='btn btn-secondary', onclick="window.history.back()")
            )

        if self.instance and self.instance.pk:
            self.helper.add_input(
                Submit('delete', 'Delete', css_class='btn btn-danger', onclick="return confirm('Are you sure you want to delete this user?');")
            )