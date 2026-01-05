from django.db import models
from django.utils import timezone


# Create your models here.
class Admins(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Add_news(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=timezone.now)
