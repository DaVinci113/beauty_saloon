from datetime import datetime as dt
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee, Service, Client, Record
from calendar import HTMLCalendar


# Create your views here.


class Index(TemplateView):
    template_name = 'saloon/index.html'


class EmployeeListView(ListView):
    model = Employee
    template_name = 'saloon/employee_list.html'
    context_object_name = 'employees'


class ShowEmployeeDetail(DetailView):
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
    
    
class EmployeeDeleteView(DeleteView):
    model = Employee
    pk_url_kwarg = 'employee_pk'
    template_name = 'saloon/delete.html'
    success_url = '/employee_list'


class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'saloon/create.html'
    success_url = '/employee_list'


class SpecialityEmployeeList(DetailView):
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
    
    
class GraficView(HTMLCalendar, TemplateView):
    template_name = 'saloon/grafic.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = dt.now()
        year = date.year
        month = date.month
        # year = 2024
        # month = 12
        context['calendar_month'] = HTMLCalendar().formatmonth(year, month)
        if month < 12:
            context['calendar_next_month'] = HTMLCalendar().formatmonth(year, month+1)
        else:
            context['calendar_next_month'] = HTMLCalendar().formatmonth(year+1, 1)
        return context
    
    
class RecordListView(ListView):
    model = Record
    template_name = 'saloon/record_list.html'
    context_object_name = 'records'
    
    
class RecordCreateView(CreateView):
    model = Record
    fields = ['client', 'service', 'employee']
    template_name = 'saloon/record_create.html'
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = dt.today()
        context['current_date'] = dt.strftime(today, '%Y-%m-%d')
        context['current_time'] = dt.strftime(today, '%H:%M')
        return context
    
    def post(self, request, *args, **kwargs):
        client = Client.objects.get(pk=self.request.POST['client'])
        service = Service.objects.get(pk=self.request.POST['service'])
        employee = Employee.objects.get(pk=self.request.POST['employee'])
        date = self.request.POST['input_date']
        time = self.request.POST['input_time']
        record = Record(
            client=client,
            service=service,
            employee=employee,
            record_date=date,
            record_time=time,
        )
        record.save()
        return redirect('saloon:home')
        