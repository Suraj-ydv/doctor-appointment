from django.db import models
from doctorapp.models import Doctor_reg


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()


class Customer_reg(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    city = models.CharField(max_length=50)


class Customer_pic(models.Model):
    name = models.ForeignKey(Customer_reg,on_delete=models.CASCADE)
    customer_Img = models.ImageField(upload_to='images/')


class Customer_query(models.Model):
    email = models.EmailField(max_length=50)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    doctor_name = models.ForeignKey(Doctor_reg, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    dr_response = models.TextField(max_length=200, blank=True)
    dr_response_date = models.DateField(blank=True, null=True)


class Book_appointment(models.Model):
    customer_name = models.ForeignKey(Customer_reg, on_delete=models.CASCADE)
    doctor_name = models.ForeignKey(Doctor_reg, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason_for_appointment = models.TextField(max_length=200)
    prescription = models.TextField(max_length=200)
    file = models.FileField(upload_to='files/')
    status=models.CharField(max_length=50,default="waiting")