from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
 
# Create your models here.
class Profile(AbstractUser):
    userRole = models.CharField(max_length=50, default =False)
    gender = models.CharField(max_length=50, default =False)
    age = models.IntegerField(default =False)
    category = models.CharField(max_length=50, default =False)
    #certification = models.FileField(max_length=100,default ='default_file.txt',upload_to='uploads/certifications' )

class Program(models.Model):
   name = models.CharField(max_length=51)
   description = models.CharField(max_length=101)
   start_date = models.DateField()
   end_date = models.DateField()
   duration = models.CharField(max_length=51)
   level = models.CharField(max_length=51)
   location = models.CharField(max_length=51)
   seats = models.IntegerField()
   
 
    

