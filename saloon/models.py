from django.db import models


# Create your models here.


class Speciality(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    specialization = models.ManyToManyField(Speciality, related_name='specializations')
    birdth_data = models.DateTimeField(verbose_name='Дата рождения')
    
    def __str__(self):
        return f'{self.last_name} {self.name}'
