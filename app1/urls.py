from django.urls import path
from .views import CreateView, ReadView

urlpatterns = [
    path('films/', CreateView.as_view(), name='films'),
    path('films/<int:pk>', ReadView.as_view(), name='read')
]
