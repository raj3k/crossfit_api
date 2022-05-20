from django.urls import path
from .views import WorkoutListAPIView

# /api/
urlpatterns = [
    path('', WorkoutListAPIView.as_view()),
]