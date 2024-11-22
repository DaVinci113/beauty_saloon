from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Employee, Service


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
    
    
class SpecialityEmployeeList(DetailView):
    model = Service
    template_name = 'saloon/service_employee_list.html'
    pk_url_kwarg = 'service_pk'
    context_object_name = 'service'


class EmployeeCreateView(CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'saloon/create.html'
    success_url = '/employee_list'


class ServicesListView(ListView):
    model = Service
    template_name = 'saloon/services_list.html'
    context_object_name = 'services'
    
    
class ServiceCreateView(CreateView):
    model = Service
    fields = '__all__'
    template_name = 'saloon/create.html'
    success_url = '/services_list'
    