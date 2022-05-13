import uuid
from django.db import models


class Workout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    mode = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trainer_tips = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    

class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="workout_exercises")
    content = models.TextField()

    def __str__(self) -> str:
        return self.content


class Equipment(models.Model):
    name = models.CharField(max_length=120)
    workouts = models.ManyToManyField(Workout, related_name="equipment")

    def __str__(self) -> str:
        return self.name