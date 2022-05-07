from rest_framework import serializers
from .models import Workout, Equipment, Exercise


class WorkoutSerializer(serializers.ModelSerializer):
    equipment = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    exercises = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Workout
        fields = '__all__'
