from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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

class TaskCreate(CreateView):
    model = Task
    template_name = 'ToDo_App/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'ToDo_App/task_form.html'
    success_url = reverse_lazy('home')