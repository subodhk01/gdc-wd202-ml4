
from django.urls import path
from django.shortcuts import render, HttpResponseRedirect

tasks = []
completed_tasks = []

def tasks_view(request):
    print('tasks: ', tasks)
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def completed_tasks_view(request):
    print('completed_tasks: ', completed_tasks)
    return render(request, 'completed_tasks.html', {
        'tasks': completed_tasks
    })

def add_new_task(request):
    print('request get: ', request.GET)
    tasks.append( request.GET.get('task') )
    return HttpResponseRedirect('/tasks/')

def delete_task(request, index):
    del tasks[index - 1]
    return HttpResponseRedirect('/tasks/')

def complete_task(request, index):
    completed_tasks.append( tasks[index - 1] )
    del tasks[index - 1]
    return HttpResponseRedirect('/tasks/')

urlpatterns = [
    path('tasks/', tasks_view, name='all-tasks'),
    path('completed_tasks/', completed_tasks_view, name='completed-tasks'),
    path('add-task/', add_new_task, name="add-task"),
    path('delete-task/<int:index>/', delete_task, name="delete-task"),
    path('complete_task/<int:index>/', complete_task, name="complete-task"),

]
