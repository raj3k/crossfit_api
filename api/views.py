from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from wods.models import Workout



@api_view(["GET"])
def index(request):
    model_data = Workout.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["name", "mode"])
    return Response(data)