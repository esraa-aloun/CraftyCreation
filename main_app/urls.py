from django.urls import path 
# from route import views
from . import views 

# import chagne view
from django.contrib.auth.views import PasswordChangeView , PasswordChangeDoneView

urlpatterns =[
    path('', views.home, name='home' ),
    path('about/', views.about, name='about'),   
    path('accounts/signup', views.signup, name='signup'),
    path('joinProgram/<int:program_id>', views.Register_Student_Into_Program, name='joinProgram'),   
    path('profile/', views.profile, name='profile'),  
    # path('studentList/<int:program_id>', views.student_list, name='studentList'),  
    path('studentList/<int:passed_program_id>', views. student_list.as_view(), name='studentList'),  
    path('program/', views.ProgramBrowse.as_view(), name='program'),
    path('programForInstructor/', views.ProgramList.as_view(), name='programForInstructor'),
    path('my_programs/', views.My_Programs.as_view(), name='my_programs'),
    path('addProgram/', views.ProgramCreate.as_view(), name='addProgram'),
    path('accounts/change_password/',PasswordChangeView.as_view(template_name='registration/change_password.html'), name ='change_password'),

]