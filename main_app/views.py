from django.shortcuts import render, redirect, get_object_or_404
from main_app.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
import logging
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse
from .models import Program, Profile, RegisteredStudent
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):   
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# def program(request):
#     return render(request, 'program.html')

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

@login_required
def profile(request):
    user= request.user
    
    return render(request, 'profile.html' , 
    {'user':user ,
     'profile': profile,
    })

class ProgramCreate(CreateView):
    model = Program   
    fields = ['name','description','start_date','end_date','duration','level','location','seats']
     
    def form_valid(self, form):
        form.instance.instructor = self.request.user
        # logging.debug(self.request.session.get('user_id'))
        return super().form_valid(form)
     
    success_url='/'
          
class ProgramList(ListView):
    model = Program
    def get_queryset(self):
        return Program.objects.filter(instructor=self.request.user)
    
# Delete
# Edit
    
class ProgramBrowse(ListView):
    template_name = 'main_app/program_browser.html'
    model = Program


def Register_Student_Into_Program(request, program_id):
    student = request.user
    print(student)
    program = Program.objects.get(id = program_id)
    studentProgram = RegisteredStudent(program_id = program, student_id= student)
    studentProgram.save()
    program.seats -= 1
    program.save()
    
        
    return render(request, 'home.html', {'message': 'You joined the class successfully!'})





  
     