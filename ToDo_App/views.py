from django import forms
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from .forms import CustomLoginForm, CustomSignupForm, CustomTaskCreateForm
from .models import Task

# Create your views here.


class Register(FormView):
    template_name = 'ToDo_App/register.html'
    form_class = CustomSignupForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Register, self).get(*args, **kwargs)



class Login(LoginView):
    template_name = 'ToDo_App/login.html'
    authentication_form = CustomLoginForm
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
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__startswith=search_input)

        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'ToDo_App/task_detail.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'ToDo_App/task_form.html'
    form_class = CustomTaskCreateForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'ToDo_App/task_update.html'
    form_class = CustomTaskCreateForm
    success_url = reverse_lazy('home')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'ToDo_App/task_delete.html'
    success_url = reverse_lazy('home')


