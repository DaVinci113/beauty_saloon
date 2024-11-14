from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render


# Create your views here.


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': 'Авторизация'}


class LogoutUser(LogoutView):
    form_class = AuthenticationForm
    template_name = 'users:logout'
    extra_context = {'title': 'Выход'}
