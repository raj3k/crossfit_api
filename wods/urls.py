from django.urls import path
from .views import WorkoutListAPIView, WorkoutDetailAPIView

# /api/workouts/
urlpatterns = [
    path('', WorkoutListAPIView.as_view()),
    path('<uuid:pk>', WorkoutDetailAPIView.as_view())
]