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
        fields = ['id', 'name', 'mode', 'equipment', 'exercises', 'created_at', 'updated_at', 'trainer_tips']
