from django.contrib import admin
from .models import Category, Film, FilmListRecommendation, User

# Register your models here.
admin.site.register(Category)
admin.site.register(Film)
admin.site.register(User)
admin.site.register(FilmListRecommendation)