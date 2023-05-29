from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, SignInForm


# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "User created successfully")
            return redirect("home")

    return render(request, "signup.html", {"form": form})


def signin(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = SignInForm()

    if request.method == "POST":
        form = SignInForm(request.POST)
        print(request.POST)
        print()
        print(form)
        if form.is_valid():
            print(form.cleaned_data)

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(username=username, password=password)
            # Credentials were already checked in the form, so this is unnecessary, but whatever
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful")
                return redirect("home")

    return render(request, "signin.html", {"form": form})


@login_required
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("home")
