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
    content = models.TextField()
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content


class Equipment(models.Model):
    name = models.CharField(max_length=120)
    workouts = models.ManyToManyField(Workout)

    def __str__(self) -> str:
        return self.name