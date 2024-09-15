from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, PasswordInput


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label="Password",
        widget=PasswordInput(attrs={"class": "form-control"})
    )
    password2 = forms.CharField(label="Confirm Password",
        widget=PasswordInput(attrs={"class": "form-control"})
    )
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Extract the request object
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": TextInput(attrs={"class": "form-control"}),
            "email": EmailInput(attrs={"class": "form-control"}),
        }

