from django.db import models


# Create your models here.
class Doctor_reg(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    mobile = models.BigIntegerField()
    qualification = models.CharField(max_length=50)
    specialization = models.CharField(max_length=50)
    appointment_fee = models.IntegerField()
    experience = models.CharField(max_length=50)
    about_me = models.TextField()
    city = models.CharField(max_length=50)


class Doctor_pic(models.Model):
    name = models.ForeignKey(Doctor_reg,on_delete=models.CASCADE)
    doctor_Img = models.ImageField(upload_to='images/')


class Add_schedule(models.Model):
    email = models.EmailField(max_length=50)
    available_date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()
