from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task


# Create your views here.

class Login(LoginView):
    template_name = 'ToDo_App/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
    

class Home(LoginRequiredMixin, ListView):
    model = Task    
    template_name = 'home.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'ToDo_App/task_detail.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'ToDo_App/task_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    template_name = 'ToDo_App/task_form.html'
    success_url = reverse_lazy('home')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'ToDo_App/task_delete.html'
    success_url = reverse_lazy('home')


