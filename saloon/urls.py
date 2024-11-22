from django.urls import path
from . import views

app_name = 'saloon'
urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('employee_list/', views.EmployeeListView.as_view(), name='employee-list'),
    path('employee_create/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('employee_detail/<int:employee_pk>/', views.ShowEmployeeDetail.as_view(), name='employee-detail'),
    path('employee_update/<int:employee_pk>/', views.EmployeeUpdateView.as_view(), name='employee-update'),
    path('service_employee_list/<int:service_pk>/', views.SpecialityEmployeeList.as_view(), name='service_employee_list'),
    path('services_list/', views.ServicesListView.as_view(), name='services-list'),
    path('service_create/', views.ServiceCreateView.as_view(), name='service-create'),
    
]
