from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Masukan Username',
        'class': 'form-control',
        'autocomplete': 'off',
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Masukan Username',
        'class': 'form-control',
        'autocomplete': 'off',
    }))