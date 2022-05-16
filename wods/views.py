from rest_framework import generics
from rest_framework import mixins
from .models import Workout, Equipment, Exercise
from .serializers import WorkoutSerializer


class WorkoutListAPIView(generics.ListCreateAPIView):
    """
    List all Workout instances and create new Workout instance.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class WorkoutDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, partialy update and delete Workout instance.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    lookup_field = 'pk'


