from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import TaskRoomForm
from .models import TasksRoom, Task


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

                if room.users.filter(id=request.user.id).exists():
                    messages.error(request, f"You are already in the room {room.title}")
                    return redirect("home")
                else:
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


@login_required
def room(request, hash):
    context = {
        "hash": hash,
    }

    # Current room
    current_room = TasksRoom.objects.get(id_room=hash)
    context["users"] = current_room.users.all()

    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        importance = request.POST["importance"]
        room = current_room

        # Create task
        t = Task.objects.create(
            title=title, description=description, room=room, importance=importance
        )
        messages.success(request, "Task created successfully")

    # Get the room title
    context["room_title"] = current_room.title

    # Stablish empty lists for iterate over all the tasks, otherwise will save only one task
    context["todo_tasks"] = []
    context["inprogress_tasks"] = []
    context["done_tasks"] = []

    tasks = Task.objects.filter(room=hash)
    for current_task in tasks:
        if current_task.current_state == "TODO":
            context["todo_tasks"].append(current_task)
        elif current_task.current_state == "INPROG":
            context["inprogress_tasks"].append(current_task)
        else:
            context["done_tasks"].append(current_task)

    return render(request, "tasksroom.html", context=context)


@login_required
def leave(request, hash):
    room = TasksRoom.objects.get(id_room=hash)

    if room.users.filter(id=request.user.id).exists():
        room.users.remove(request.user)
        messages.success(request, "You have successfully left the room")

    return redirect("home")


@login_required
def update(request, hash, task_id):
    if request.method == "POST":
        # Get current room
        room = TasksRoom.objects.get(id_room=hash)

        # Check if the task exists
        if Task.objects.filter(id=task_id).exists():
            # Check if the task is in the room
            if room.task_set.filter(id=task_id).exists():
                task = room.task_set.get(id=task_id)
                task.title = request.POST["title"]
                task.description = request.POST["description"]
                task.importance = request.POST["importance"]
                task.current_state = request.POST["current_state"]
                task.save()

                messages.success(request, "Task updated")

    redirect_url = reverse("room", kwargs={"hash": hash})
    return redirect(redirect_url)


@login_required
def delete(request, hash, task_id):
    # Get current room
    room = TasksRoom.objects.get(id_room=hash)

    # Check if the task exists
    if Task.objects.filter(id=task_id).exists():
        # Check if the task is in the room
        if room.task_set.filter(id=task_id).exists():
            Task.objects.filter(id=task_id).delete()
            messages.success(request, "Task deleted!")

    redirect_url = reverse("room", kwargs={"hash": hash})
    return redirect(redirect_url)
