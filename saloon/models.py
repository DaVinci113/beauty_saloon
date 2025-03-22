from django.db import models
# from users.models import User


# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Услуга')
    price = models.IntegerField(verbose_name='Примерная стоимость')
    duration = models.IntegerField(verbose_name='Продолжительность (минуты)')
    
    def __str__(self):
        return f'{self.name} ~{self.price}руб'
    
    class Meta:
        ordering = ['name']


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    specialization = models.ManyToManyField(Service, verbose_name='Услуги мастера', related_name='specialization')
    birdth_data = models.DateField(verbose_name='Дата рождения (в формате: ГГГГ-ММ-ДД)')
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['last_name', 'name']


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='Имя клиента')
    last_name = models.CharField(null=True, blank=True, max_length=25, verbose_name='Фамилия клиента')
    phone_number = models.IntegerField(verbose_name='Номер телефона')
    
    def __str__(self):
        return f'тел: {self.phone_number} {self.last_name} {self.name}'
    
    class Meta:
        ordering = ['last_name', 'name', 'phone_number']


class Record(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name='Мастер')
    record_date = models.DateField(verbose_name='Назначенная дата')
    record_time = models.TimeField(verbose_name='Назначенное время')
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name='Время регистрации записи')
    
    class Meta:
        ordering = ['record_date', 'record_time']
    
    def __str__(self):
        return f'{self.client} \n дата записи: {self.record_date} время: {self.record_time}'
