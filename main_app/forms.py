from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile, Category, Program

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
    email = forms.EmailField(label='Email')
      

    class Meta:
        model = Profile
        fields = ["username", "email", "password1", "password2","userRole","gender","age"]
        #fields = '__all__'

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
    
# LEVELS = (
#     ('Beginner','Beginner'),
#     ('Intermediate','Intermediate'),
#     ('Expert','Expert')
# )
    
# class AddProgramm(forms.ModelForm):
#     cat_name = forms.ModelChoiceField(queryset=Category.objects.all())
#     level = forms.ChoiceField(
#            choices= LEVELS
#         )
#     class Meta:
#         model = Program
#         fields = ['name', 'description','start_date','end_date','duration','level','location','seats']
        
    
# #  upload file form
# class UploadFileForm(forms.Form):
#     file= forms.FileField()