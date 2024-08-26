"""
URL configuration for recommendations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app1.views import LoginView, RegisterView, CreateRecommendationView, CreateFilmView, LandingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingView.as_view(), name="landing"),
    path('createRecommendation/', CreateRecommendationView.as_view(), name="createRecommendation"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('createfilm/', CreateFilmView.as_view(), name="createFilm"),
    path('api/', include('app1.urls'))

]
