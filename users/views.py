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
