from django.contrib import admin
from .models import Profile, Program, RegisteredStudent


# Register your models here.

admin.site.register(Profile)
admin.site.register(Program)
admin.site.register(RegisteredStudent)
