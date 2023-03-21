from django.urls import path 
# from route import views
from . import views 
urlpatterns =[
    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),   
    path('accounts/signup', views.signup, name='signup'),
    path('joinProgram/<int:program_id>', views.Register_Student_Into_Program, name='joinProgram'),   
  
    path('program/', views.ProgramBrowse.as_view(), name='program'),
    path('programForInstructor/', views.ProgramList.as_view(), name='programForInstructor'),
    path('addProgram/', views.ProgramCreate.as_view(), name='addProgram')
]