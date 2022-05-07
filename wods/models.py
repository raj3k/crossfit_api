import uuid
from django.db import models


class Exercise(models.Model):
    name = models.TextField()

    def __str__(self) -> str:
        return self.name
    


class Equipment(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.name


class Workout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120)
    mode = models.CharField(max_length=120)
    equipment = models.ManyToManyField(Equipment)
    exercises = models.ManyToManyField(Exercise)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    trainer_tips = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    

