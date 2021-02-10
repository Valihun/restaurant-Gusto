from django.db import models
from uuid import uuid4
import os


# Create your models here.


class Category(models.Model):

    def get_file_name_category(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join('images/category/', filename)

    title = models.CharField(max_length=50)
    category_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    is_special = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_file_name_category)

    def __str__(self):
        return f'{self.title} : {self.category_order}'


class Dish(models.Model):

    def get_file_name_dishes(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)

    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    is_visible = models.BooleanField(default=True)
    description = models.CharField(max_length=300, null=True)
    photo = models.ImageField(upload_to=get_file_name_dishes)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Event(models.Model):

    def get_file_name_events(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)

    title = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=get_file_name_events)
    description = models.TextField(null=True)
    event_date = models.DateField()
    event_time = models.TimeField()
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f'{self.title} : {self.event_date}'


class Banners(models.Model):

    def get_file_name_banners(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)

    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=get_file_name_banners)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'


class UserMessages(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    message = models.CharField(max_length=200)

    is_processed = models.BooleanField(default=False)
    send_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name}-{self.user_email}: {self.message[:20]}'


class Info(models.Model):

    def get_file_name_info(self, filename):
        ext = filename.split('.')[-1]
        filename = f'{uuid4()}.{ext}'
        return os.path.join('images/info/', filename)

    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=get_file_name_info)
    discription = models.TextField(null=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'
