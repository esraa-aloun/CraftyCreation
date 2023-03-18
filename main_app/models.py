from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
 
# Create your models here.
class Profile(AbstractUser):
    userRole = models.CharField(max_length=50, required= True),
    gender = models.CharField(max_length=50, required= True),
    age = models.IntegerField(max_length=50, required= True),
    category = models.CharField(max_length=50, default = 'default'),
    certification = models.FileField(max_length=100, default ='default_file.txt')
