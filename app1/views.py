from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, CreateView
# Create your views here.
import psycopg2
from config import load_config
import csv
from .serializers import FilmSerializer
from rest_framework import generics
from .models import Film
from .forms import UserForm
from .models import User

class LandingView(TemplateView):
    template_name = "landing.html"

class CreateRecommendationView(TemplateView):
    template_name = "createRecommendation.html"

class LoginView(TemplateView):
    template_name = "login.html"

class UserCreateView(CreateView):
    model = User
    template_name = "register.html"
    form_class = UserForm
    success_url = "/"
    
    def form_valid(self, form):
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        print(first_name, last_name, email, password)
        return super().form_valid(form)
    
class CreateView(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    
class CreateFilmView(TemplateView):
    template_name = "createFilm.html"




