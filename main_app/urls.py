from django.urls import path 
# from route import views
from . import views 

# import chagne view
from django.contrib.auth.views import PasswordChangeView , PasswordChangeDoneView

urlpatterns =[
    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),   
    path('accounts/signup', views.signup, name='signup'),
   
  
    path('program/', views.program, name='program'),
    path('addProgram/', views.ProgramCreate.as_view(), name='addProgram'),

    path('profile/', views.profile, name='profile'),

    # upload file 
    path('upload/', views.upload_file , name="upload"),

    # change password: 
    path('accounts/change_password/',PasswordChangeView.as_view(template_name='registration/change_password.html'), name ='change_password'),
]