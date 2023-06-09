from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
 
# Create your models here.
GENDER = (
    ('F','Female'),
    ('M','Male')
)
UserRoles = (
    ('I','Instructor'),
    ('S','Student')
)
class Profile(AbstractUser):
    userRole = models.CharField( 
        max_length=1,   
        choices= UserRoles,
        default = UserRoles[0][0])

    gender = models.CharField(
        max_length=1,
        choices=GENDER,
        default =GENDER[0][0]
        )
    age = models.IntegerField(default =False)
    category = models.CharField(max_length=50, default =False)
    # uploading the instructer certificate
    # certification = models.FileField(default ='',upload_to='main_app/static/uploads' )

class Program(models.Model):
   name = models.CharField(max_length=51)
   description = models.CharField(max_length=101)
   start_date = models.DateField()
   end_date = models.DateField()
   duration = models.CharField(max_length=51)
   level = models.CharField(max_length=51)
   location = models.CharField(max_length=51)
   seats = models.IntegerField()
   instructor = models.ForeignKey(Profile, on_delete=models.CASCADE)

   def get_absolute_url(self):
         return reverse('home')
        
   
 
    

