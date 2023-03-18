from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, User


class UserCreationForm(UserCreationForm):
    userRole = forms.CharField(max_length=50),
    gender = forms.CharField(max_length=50),
    age = forms.IntegerField(max_length=50),
    category = forms.CharField(max_length=50),
    certification = forms.FileField(max_length=100)
   

    class Meta:
        model = Profile
        fields = ("username", "email", "password1", "password2","userRole","gender","age","category","certification")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user