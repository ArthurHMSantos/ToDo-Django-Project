from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Task

# Create your views here.
class Home(ListView):
    model = Task    
    template_name = 'home.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = 'ToDo_App/task_detail.html'
    context_object_name = 'task'