from rest_framework import generics

from .models import Workout, Equipment, Exercise
from .serializers import WorkoutSerializer


class WorkoutListAPIView(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class WorkoutDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


