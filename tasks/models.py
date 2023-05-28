import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TasksRoom(models.Model):
    id_room = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    title = models.CharField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title} | {self.id_room}"


class Task(models.Model):
    title = models.CharField(
        required=True,
        blank=False,
    )
    description = models.CharField()
    room = models.ForeignKey(TasksRoom, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return -1
