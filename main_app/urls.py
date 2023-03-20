from django.urls import path 
# from route import views
from . import views 
urlpatterns =[
    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),   
    path('accounts/signup', views.signup, name='signup'),
  
    path('program/', views.program, name='program'),
    path('addProgram/', views.ProgramCreate.as_view(), name='addProgram')
]