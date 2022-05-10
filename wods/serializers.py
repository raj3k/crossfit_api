from rest_framework import serializers
from .models import Workout, Equipment, Exercise


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['name']


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['name']



class WorkoutSerializer(serializers.ModelSerializer):
    # equipment = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    # )

    # exercises = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    # )
    equipment = EquipmentSerializer(many=True)
    exercises = ExerciseSerializer(many=True)


    class Meta:
        model = Workout
        fields = ['id', 'name', 'mode', 'equipment', 'exercises', 'created_at', 'updated_at', 'trainer_tips']

    def create(self, validated_data):
        equipment_data = validated_data.pop('equipment')
        exercises_data = validated_data.pop('exercises')
        workout = Workout.objects.create(**validated_data)
        for equipment in equipment_data:
            workout.equipment.create(**equipment)

        for exercise in exercises_data:
            workout.exercises.create(**exercise)
        return workout
        
    def update(self, instance, validated_data):
        pass
