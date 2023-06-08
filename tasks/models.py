import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TasksRoom(models.Model):
    id_room = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=True, max_length=500)
    users = models.ManyToManyField(User, related_name="rooms")

    def __str__(self):
        return f"{self.title} | {self.id_room}"


class Task(models.Model):
    IMPORTANCE_CHOICES = (
        ("HIG", "High"),
        ("MED", "Medium"),
        ("LOW", "Low"),
    )

    CURRENT_STATE = (
        ("TODO", "TO-DO"),
        ("INPROG", "In Progress"),
        ("DONE", "Done"),
    )

    title = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=True, max_length=500)
    room = models.ForeignKey(TasksRoom, on_delete=models.CASCADE)
    importance = models.CharField(
        choices=IMPORTANCE_CHOICES, default="", blank=True, max_length=10
    )
    current_state = models.CharField(
        choices=CURRENT_STATE, default="TODO", blank=True, max_length=10
    )

    def __str__(self):
        return f"{self.title} | {self.room}"
