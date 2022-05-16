from rest_framework import generics
from rest_framework import mixins
from .models import Workout, Equipment, Exercise
from .serializers import WorkoutSerializer


class WorkoutListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    """
    List all Workout instances and create new Workout instance.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class WorkoutDetailAPIView(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update and delete Workout instance.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


