from django.shortcuts import render, redirect
from main_app.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
import logging
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Program

# Create your views here.
def home(request):   
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        #logging.basicConfig(level=logging.DEBUG)
        logging.debug(request.POST)
        print(form.errors)
        if form.is_valid():

            user = form.save()
            login(request, user)
            return redirect("home")
        else:
           
            messages.error(request, "Invalid form entries")
    form = UserCreationForm()
    context = {"form": form}
    return render(request, "registration/signup.html", context)

class ProgramCreate(CreateView):
     model = Program   
     fields = '__all__'  

     success_url='/'

     

  
     