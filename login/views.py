from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.db import IntegrityError
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register(request):
    form = UserCreationForm
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect("home")
            except IntegrityError:
                print("error")

    return render(request, "register.html", {"form": form})


def sign(request):
    if request.method == "GET":
        return render(request, "login.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "login.html",
                {
                    "form": AuthenticationForm,
                    "error": "Username or password is incorrect.",
                },
            )

        login(request, user)
        return redirect("home")


def exit(request):
    logout(request)
    return redirect("welcome")


def welcome(request):
    return render(request, "welcome.html")


@login_required
def home(request):
    tasks = Task.objects.filter(user = request.user)
    title = "task list"
    form = TaskForm
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("home")
    return render(request, "home.html", {"tasks": tasks, "title": title, "form": form})


@login_required
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect("/")


@login_required
def detail_task(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, "details.html", {"task": task})


@login_required
def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    return render(request, "form.html", {"task": task, "form": form})
