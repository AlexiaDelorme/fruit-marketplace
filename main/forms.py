from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserType


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignupForm(UserCreationForm):

    USER_TYPES_CHOICES = [
        ('A', 'Farmer'),
        ('B', 'Client')
    ]

    email = forms.EmailField()

    user_type = forms.CharField(
        widget=forms.Select(
            choices=USER_TYPES_CHOICES),
        label="Register as farmer or client?"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'user_type', 'password1', 'password2']
