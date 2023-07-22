from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Task

# Create your views here.
class Home(ListView):
    model = Task    
    template_name = 'home.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task'