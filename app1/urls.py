from django.urls import path
from .views import CreateView

urlpatterns = [
    path('films/', CreateView.as_view(), name='films'),
   
]
