from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("home/<uuid:hash>", views.room, name="room"),
    path("home/<uuid:hash>/leave", views.leave, name="leave"),
    path("home/<uuid:hash>/update/<int:task_id>", views.update, name="update"),
    path("home/<uuid:hash>/delete/<int:task_id>", views.delete, name="delete"),
]
