from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from wods.models import Workout
from wods.serializers import WorkoutSerializer



@api_view(["GET"])
def api_home(request):
    instance = Workout.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = WorkoutSerializer(instance).data
    return Response(data)