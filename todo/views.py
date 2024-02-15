from typing import Any
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Task 
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import login, logout
from django.http import HttpResponse
# Create your views here.

class UserLogin(LoginView):
    template_name = "todo/login.html"
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy("todo:tasks_list")
    

    
    
class RegisterView(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True 
    success_url = reverse_lazy("todo:tasks_list")
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("todo:tasks_list")
        return super(RegisterView, self).get(*args, **kwargs)
        


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'todo/tasks_list.html'
    
    #each user gets their own data 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(is_done=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
            
        context['search_input'] = search_input
        return context
        
    
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task_detail'
    template_name = 'todo/task_detail.html'
    
class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'discription', 'is_done']
    success_url = reverse_lazy('todo:tasks_list')
    template_name = 'todo/create_task.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super(CreateTask, self).form_valid(form)
    

class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task 
    fields = ['title', 'discription', 'is_done']
    success_url = reverse_lazy('todo:tasks_list')
    template_name = 'todo/create_task.html'
    
    
    
class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'tasks'
    success_url = reverse_lazy('todo:tasks_list')
    template_name = 'todo/delete_task.html'


def logout_user(request):
    logout(request)
    return HttpResponse("You are logged out")
