from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskRoomForm
from django.contrib import messages
from .models import TasksRoom, Task
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import HttpResponse


# Create your views here.
@login_required
def home(request):
    context = {}

    formRoom = TaskRoomForm()

    if request.method == "POST":
        # Button CREATE
        if "create" in request.POST:
            formRoom = TaskRoomForm(request.POST)
            if formRoom.is_valid():
                form_instance = formRoom.save(commit=True)
                form_instance.users.add(request.user)

                room_hash = form_instance.id_room
                redirect_url = reverse("room", kwargs={"hash": room_hash})

                messages.success(request, "Room created successfully")
                return redirect(redirect_url)
            else:
                messages.error(request, "A error occurred while creating")
        # Button ENTER
        else:
            room_hash = request.POST["room_hash"]
            if TasksRoom.objects.filter(id_room=room_hash).exists():
                room = TasksRoom.objects.get(id_room=room_hash)
                room.users.add(request.user)
                messages.success(request, "You entered the room successfully!")
                redirect_url = reverse("room", kwargs={"hash": room_hash})
                return redirect(redirect_url)
            else:
                messages.error(request, "A error occurred while entering")

    context["formRoom"] = formRoom
    rooms = TasksRoom.objects.filter(users=request.user)
    context["rooms"] = rooms
    return render(request, "home.html", context)


def room(request, hash):
    return HttpResponse("Romm id: " + str(hash))
