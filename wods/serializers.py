from rest_framework import serializers
from .models import Workout, Equipment, Exercise
from typing import List, OrderedDict, Any


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

    def create(self, validated_data: dict[Any]) -> Workout:
        print(type(validated_data))
        workout_exercises_data: List(OrderedDict) = validated_data.pop('workout_exercises')
        equipment_data: List[OrderedDict] = validated_data.pop('equipment')

        workout_instance: Workout = Workout.objects.create(**validated_data)

        for exercise in workout_exercises_data:
            Exercise.objects.create(workout=workout_instance, **exercise)

        for equipment in equipment_data:
            if not Equipment.objects.filter(name__iexact=equipment['name']):
                workout_instance.equipment.create(name=equipment['name'])
            else:
                workout_instance.equipment.add(Equipment.objects.get(name__iexact=equipment['name']))
        
        return workout_instance

    def update(self, instance: Workout, validated_data: dict[Any]):
        workout_exercises_data: List[OrderedDict] = validated_data.pop('workout_exercises')
        equipment_data: List[OrderedDict] = validated_data.pop('equipment')
        workout_equipment_ids: List[int] = [e.equipment_id for e in instance.equipment.through.objects.filter(workout_id=instance.id)]


        for equipment in equipment_data:
            if not instance.equipment.filter(name__iexact=equipment['name']).exists():
                if not Equipment.objects.filter(name__iexact=equipment['name']):
                    instance.equipment.create(name=equipment['name'])
                else:
                    instance.equipment.add(Equipment.objects.get(name=equipment['name']))

        for i in workout_equipment_ids:
            if not i in [Equipment.objects.get(name__iexact=e['name']).id for e in equipment_data]:
                instance.equipment.through.objects.get(equipment_id=i).delete()
        

        for e in instance.workout_exercises.all():
            if not e.content in [ex['content'] for ex in workout_exercises_data]:
                e.delete()

        for exercise in workout_exercises_data:
            if not instance.workout_exercises.filter(content__iexact=exercise['content']):
                instance.workout_exercises.create(**exercise)

        return super().update(instance, validated_data)