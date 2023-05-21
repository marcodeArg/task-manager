from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, SignInForm


# Create your views here.
def signup(request):
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "User created successfully")
            return redirect("home")

    return render(request, "signup.html", {"form": form})


def signin(request):
    form = SignInForm()

    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "Login successful")
            return redirect("home")

    return render(request, "signin.html", {"form": form})


def logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")
