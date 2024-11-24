from django.urls import path
from .views import *

app_name = 'saloon'
urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('employee_list/', EmployeeListView.as_view(), name='employee-list'),
    path('employee_create/', EmployeeCreateView.as_view(), name='employee-create'),
    path('employee_detail/<int:employee_pk>/', ShowEmployeeDetail.as_view(), name='employee-detail'),
    path('employee_update/<int:employee_pk>/', EmployeeUpdateView.as_view(), name='employee-update'),
    path('service_employee_list/<int:service_pk>/', SpecialityEmployeeList.as_view(), name='service_employee_list'),
    path('services_list/', ServicesListView.as_view(), name='services-list'),
    path('service_create/', ServiceCreateView.as_view(), name='service-create'),
    path('client_list/', ClientListView.as_view(), name='client-list'),
    path('client_create/', ClientCreateView.as_view(), name='client-create'),
    path('client_update/<int:client_pk>/', ClientUpdateView.as_view(), name='client-update'),
    path('client_list/<int:client_pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
    
]
