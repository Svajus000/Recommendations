from django.shortcuts import render
from django.views.generic import TemplateView, FormView
# from django.contrib.auth.views import LoginView
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.
from .serializers import FilmSerializer
from rest_framework import generics
from .models import Film
from .forms import CustomUserCreationForm

class LandingView(TemplateView):
    template_name = "landing.html"

class CreateRecommendationView(TemplateView):
    template_name = "createRecommendation.html"

class UserCreateView(FormView):
    template_name = "register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
       
class CreateView(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    
class CreateFilmView(TemplateView):
    template_name = "createFilm.html"

class FilmListView(TemplateView):
    template_name = "filmRecommendations.html"


