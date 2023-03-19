from django.urls import path 
# from route import views
from . import views 
urlpatterns =[
    path('', views.home, name='home' ),  
    path('accounts/signup', views.signup, name='signup' ),   
    path('addprogram/', views.ProgramCreate.as_view(), name='addProgram' ), 
    # path('nono/', views.nono, name='nono' )  
    ] 
