from rest_framework import serializers
from .models import Workout, Equipment, Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['content']


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['name']

    
class WorkoutSerializer(serializers.ModelSerializer):
    workout_exercises = ExerciseSerializer(many=True)
    equipment = EquipmentSerializer(many=True)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'mode', 'equipment', 'workout_exercises' ,'created_at', 'updated_at', 'trainer_tips']

    def create(self, validated_data):
        workout_exercises_data = validated_data.pop('workout_exercises')
        equipment_data = validated_data.pop('equipment')

        workout_instance = Workout.objects.create(**validated_data)

        for exercise in workout_exercises_data:
            Exercise.objects.create(workout=workout_instance, **exercise)

        for equipment in equipment_data:
            if not Equipment.objects.filter(name__icontains=equipment['name']):
                workout_instance.equipment.create(name=equipment['name'])
            else:
                workout_instance.equipment.add(Equipment.objects.get(name__icontains=equipment['name']))
        
        return workout_instance