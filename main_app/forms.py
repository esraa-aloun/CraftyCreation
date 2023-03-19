from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

UserRoles = (
    ('I','Instructor'),
    ('S','Student')
)
GENDER = (
    ('F','Female'),
    ('M','Male')
)
class UserCreationForm(UserCreationForm):
    # userRole = forms.CharField(max_length=1)
    userRole = forms.ChoiceField(
           choices= UserRoles
        )
    
    gender = forms.ChoiceField(
         choices= GENDER)
    age = forms.IntegerField()
    category = forms.CharField(max_length=50)
    # certification = forms.FileField(max_length=100)
    email = forms.EmailField(label='Email')
      

    class Meta:
        model = Profile
        fields = ["username", "email", "password1", "password2","userRole","gender","age","category"]
        #fields = '__all__'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user