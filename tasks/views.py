from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TaskRoomForm


# Create your views here.
@login_required
def home(request):
    formRoom = TaskRoomForm()

    if request.method == "POST":
        if "create" in request.POST:
            if formRoom.is_valid():
                pass

    return render(request, "home.html", {"formRoom": formRoom})
