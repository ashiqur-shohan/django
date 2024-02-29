from django.shortcuts import render, redirect
from . import forms
from task.models import TaskModel

# Create your views here.


def show_tasks(request):
    data = TaskModel.objects.all()
    return render(request, 'show_task.html', {'data': data})


def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect("show_task")
    else:
        task_form = forms.TaskForm()
    return render(request, 'add_task.html', {'form': task_form})


def edit_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect("show_task")
    return render(request, 'add_task.html', {'form': task_form})
