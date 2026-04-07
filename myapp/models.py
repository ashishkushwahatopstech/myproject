from django.db import models

# Create your models here.
class Register(models.Model):
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=10)




class Employee(models.Model):
    F_name = models.CharField(max_length=10)
    M_name = models.CharField(max_length=10)
    L_name = models.CharField(max_length=10)
    Martial_status = models.CharField()
    Email = models.EmailField()
    Contact = models.CharField(10)
    Address = models.CharField(max_length=100)
