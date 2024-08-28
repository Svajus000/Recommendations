from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
# Create your views here.
import psycopg2
from config import load_config
import csv
from .serializers import FilmSerializer
from rest_framework import generics
from .models import Film
from .forms import RegisterForm


class LandingView(TemplateView):
    template_name = "landing.html"

class CreateRecommendationView(TemplateView):
    template_name = "createRecommendation.html"

class LoginView(TemplateView):
    template_name = "login.html"

class RegisterView(FormView):
    template_name = "register.html"
    form_class = RegisterForm
    success_url = "/"
    
    def form_valid(self, form):
        print("Success")
        return super().form_valid(form)
    
class CreateView(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    
class CreateFilmView(TemplateView):
    template_name = "createFilm.html"




