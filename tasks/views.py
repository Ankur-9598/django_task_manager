# Add all your views here


from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

pending_tasks = []
completed_tasks = []

def completed_tasks_view(request):
    return render(request, "completed_tasks.html", {"tasks": completed_tasks})

def complete_task_view(request, index):
    completed_tasks.append(pending_tasks[index - 1])
    del pending_tasks[index - 1]
    return HttpResponseRedirect("/all_tasks")

def all_tasks_view(request):
    return render(request, "all_tasks.html", {"pending_tasks": pending_tasks, "completed_tasks": completed_tasks})

def tasks_view(request):
    return render(request, "tasks.html", {"tasks": pending_tasks})

def add_task_view(request):
    task_value = request.GET.get("task")
    pending_tasks.append(task_value)
    return HttpResponseRedirect("/tasks")

def delete_task_view(request, index):
    del pending_tasks[index - 1]
    return HttpResponseRedirect("/tasks")