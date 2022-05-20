from rest_framework import generics, permissions, authentication
from .models import Workout, Equipment, Exercise
from .serializers import WorkoutSerializer
from .permissions import IsWorkoutsMaintenancePermission


class WorkoutListAPIView(generics.ListCreateAPIView):
    """
    List all Workout instances and create new Workout instance.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsWorkoutsMaintenancePermission]


class WorkoutDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, partial update and delete Workout instance.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsWorkoutsMaintenancePermission]

