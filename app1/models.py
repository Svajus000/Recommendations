from typing import Any
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.http import HttpRequest
# Create your models here.

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(email=username)
#         except UserModel.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user
#         return None
    
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.category_name}"

class Film(models.Model):
    film_id = models.AutoField(primary_key=True)
    film_name = models.CharField(unique=True,max_length=50)
    rating = models.IntegerField()
    date = models.DateField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    


    def __str__(self) -> str:
        return f"{self.film_id} {self.film_name}"
    
class FilmListRecommendation(models.Model):
    list_id = models.AutoField(primary_key=True)
    list_title = models.CharField(unique=True, max_length=100)
    films = models.ManyToManyField(Film)


    def __str__(self) -> str:
        return f"{self.list_title}"
    
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True,max_length=50)
    password = models.CharField(max_length=50)
    film_list_recommendations = models.ManyToManyField(FilmListRecommendation)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"