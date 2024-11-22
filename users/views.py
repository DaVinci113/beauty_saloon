from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView

from .forms import CustomUserCreate
from users.models import User


# Create your views here.
class RegisterView(CreateView):
    form_class = CustomUserCreate
    template_name = 'users/register.html'
    success_url = '/'
    
# class LoginUser(LoginView):
#     form_class = AuthenticationForm
#     template_name = 'users/login.html'
#     extra_context = {'title': 'Авторизация'}
#
#
# class LogoutUser(LogoutView):
#     form_class = AuthenticationForm
#     template_name = 'users:logout'
#     extra_context = {'title': 'Выход'}
