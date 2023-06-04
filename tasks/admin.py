from django.contrib import admin
from .models import TasksRoom, Task
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(TasksRoom)
admin.site.register(Task)


class TasksRoomInline(admin.TabularInline):
    model = TasksRoom.users.through
    extra = 0


class CustomUserAdmin(UserAdmin):
    inlines = [TasksRoomInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
