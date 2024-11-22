from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import User


class CustomUserCreate(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'last_name', 'first_name', 'mail', 'phone_number', 'password1', 'password2',
        ]
    