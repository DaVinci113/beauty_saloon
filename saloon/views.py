from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from users.forms import CustomUserCreate
from users.models import User
from .models import Employee, Service, Client


# Create your views here.


class Index(TemplateView):
    template_name = 'saloon/index.html'


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'saloon/employee_list.html'
    context_object_name = 'employees'


class ShowEmployeeDetail(LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'saloon/employee_detail.html'
    pk_url_kwarg = 'employee_pk'
    context_object_name = 'employee'


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'saloon/create.html'
    pk_url_kwarg = 'employee_pk'
    success_url = '/employee_list'


class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'saloon/create.html'
    success_url = '/employee_list'


class SpecialityEmployeeList(LoginRequiredMixin, DetailView):
    model = Service
    template_name = 'saloon/service_employee_list.html'
    pk_url_kwarg = 'service_pk'
    context_object_name = 'service'


class ServicesListView(ListView):
    model = Service
    template_name = 'saloon/services_list.html'
    context_object_name = 'services'


class ServiceCreateView(CreateView):
    model = Service
    fields = '__all__'
    template_name = 'saloon/create.html'
    success_url = '/services_list'
    
    
class ServiceUpdateView(UpdateView):
    model = Service
    fields = '__all__'
    template_name = 'saloon/create.html'
    pk_url_kwarg = 'service_pk'
    success_url = '/services_list'
    
    
class ServiceDeleteView(DeleteView):
    model = Service
    pk_url_kwarg = 'service_pk'
    template_name = 'saloon/delete.html'
    success_url = '/services_list'


class ClientListView(ListView):
    model = Client
    fields = [
        'last_name',
        'name',
        'phone_number',
    ]
    template_name = 'saloon/client_list.html'
    context_object_name = 'clients'


class ClientCreateView(CreateView):
    model = Client
    fields = '__all__'
    template_name = 'users/register.html'
    success_url = '/client_list'
    
    
class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    template_name = 'saloon/create.html'
    pk_url_kwarg = 'client_pk'
    success_url = '/client_list'
    
    
class ClientDeleteView(DeleteView):
    model = Client
    pk_url_kwarg = 'client_pk'
    template_name = 'saloon/delete.html'
    success_url = '/client_list'
    
    
class GraficView(TemplateView):
    template_name = 'saloon/grafic.html'
    
