from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')
@login_required
def tasksPage(request):

    tasks = Task.objects.all().filter(user=request.user, detecompleted__isnull=True)
    return render(request,'tasks.html', {
        "tasks": tasks
    })
@login_required
def createTask(request):    
    if request.method == "POST":
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('tasksPage')
        except ValueError:
            return render(request,'createTask.html', {
                "form": TaskForm(),
                "error": "Ocurrio un error al crear la tarea"
            })

    return render(request,'createTask.html', {
        "form": TaskForm()
    })
@login_required
def taskDetails(request,id):
    if request.method == "GET":
        task = get_object_or_404(Task,id=id, user=request.user)
        form = TaskForm(instance=task)
        return render(request,'tasks_details.html', {
            "task": task,
            "form": form
        })
    elif request.method == "POST":
        try:
            task = get_object_or_404(Task,id=id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasksPage')
        except ValueError:
            return render(request,'tasks_details.html', {
                "task": task,
                "form": form,
                "error": "Ocurrio un error al actualizar la tarea"
            })
@login_required
def completeTask(request,id):

    task = get_object_or_404(Task,id=id, user=request.user)
    if request.method == "POST":
        task.detecompleted = timezone.now()
        task.save()
        return redirect('tasksPage')
@login_required
def deleteTask(request,id):
    task = get_object_or_404(Task,id=id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect('tasksPage')
@login_required
def tasks_terminadas(request):
    
    tasks = Task.objects.all().filter(user=request.user, detecompleted__isnull=False).order_by("-detecompleted")
    return render(request,'tasks_terminadas.html', {
        "tasks": tasks
    })