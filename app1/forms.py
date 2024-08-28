from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from .models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
        widgets = {
            "first_name" : TextInput(attrs={"class": "form-control" }),
            "last_name" : TextInput(attrs={"class": "form-control"}),
            "email" : EmailInput(attrs={"class": "form-control"}),
            "password" : PasswordInput(attrs={"class": "form-control"})
        }