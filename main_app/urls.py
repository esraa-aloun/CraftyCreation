from django.urls import path 
# from route import views
from . import views 
urlpatterns =[
    path('', views.home, name='home' )   
]