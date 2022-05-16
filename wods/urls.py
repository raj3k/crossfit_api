from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutListAPIView, WorkoutDetailAPIView


# /api/workouts/
urlpatterns = [
    path('', WorkoutListAPIView.as_view()),
    path('<uuid:pk>', WorkoutDetailAPIView.as_view())
]