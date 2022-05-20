from wods.models import Workout
from wods.serializers import WorkoutSerializer
from rest_framework import generics
from rest_framework import authentication
from rest_framework import permissions
from wods.permissions import IsWorkoutsMaintenancePermission


# TODO: to be changed
class WorkoutListAPIView(generics.ListCreateAPIView):
    """
    List all Workout instances and create new Workout instance.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser, IsWorkoutsMaintenancePermission]