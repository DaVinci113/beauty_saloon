from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    pass
    # """Кастомная модель пользователя"""
    # first_name = models.CharField(max_length=30, verbose_name='Имя')
    # last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name='Фамилия')
    # mail = models.EmailField(null=True, blank=True, verbose_name='Электронная почта')
    # phone_number = models.IntegerField(verbose_name='Номер телефона')
    #
    # @property
    # def is_authenticated(self):
    #     """Всегда возвращает True"""
    #
    #     return True
    #
    # def __str__(self):
    #     return f'{self.first_name} {self.phone_number}'
    