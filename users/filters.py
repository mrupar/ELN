from django import forms
from django_filters import FilterSet, CharFilter, ChoiceFilter
from .models import CustomUser

class UserFilter(FilterSet):
    username = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'form-control',
                },
            ),
        )
    email = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email',
                'class': 'form-control',
                },
            ),
        )
    first_name = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'class': 'form-control',
                },
            ),
        )
    last_name = CharFilter(
        lookup_expr='icontains',
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control',
                },
            ),
        )
    is_active = ChoiceFilter(
        label='',
        choices=[('', 'Active'), ('True', 'Yes'), ('False', 'No')],
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                },
            ),
        )
    is_staff = ChoiceFilter(
        label='',
        choices=[('', 'Staff'), ('True', 'Yes'), ('False', 'No')],
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                },
            ),
        )
    is_superuser = ChoiceFilter(
        label='',
        choices=[('', 'Superuser'), ('True', 'Yes'), ('False', 'No')],
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                },
            ),
        )

    
    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'is_active',
            'is_staff',
            'is_superuser',
            ]
