from django.urls import path
from .views import api_home

# /api/
urlpatterns = [
    path('', api_home),
]