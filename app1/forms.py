from django.forms import ModelForm, TextInput
from .models import User

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
        widgets = {
            "first_name" : TextInput(attrs={"class": "form-control" }),
            "last_name" : TextInput(attrs={"class": "form-control"}),
            "email" : TextInput(attrs={"class": "form-control"}),
            "password" : TextInput(attrs={"class": "form-control"})
        }