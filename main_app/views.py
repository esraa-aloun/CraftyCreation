from django.shortcuts import render, redirect, get_object_or_404
from main_app.forms import UserCreationForm
from django.contrib.auth import login
import logging
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse
from .models import Program, Profile, RegisteredStudent
from django.db.models import Q
from .models import Program
from django.contrib.auth.decorators import login_required
# Imports for uploading file
from .forms import UploadFileForm
from django.http import HttpResponse
from .models import Profile
from django.contrib import messages
from django.urls import reverse_lazy


# Change password 
from django.contrib.auth.forms import UserCreationForm ,PasswordChangeForm
from django.contrib.auth.views import PasswordChangeDoneView


# Create your views here.
def home(request):   
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# view the profile and upload the file 
@login_required
def profile(request):
    user= request.user
    
    return render(request, 'profile.html' , 
    {'user':user ,
     'profile': profile,
    })


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
    
    # success_url= reverse_lazy['home']
    # success_msg = 'nono'

#  Uplaoding certificate
def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            user_id = form.cleaned_data['profile_id']
            user = Profile.objects.get(id=user_id)
            user.certification = file
            user.save()
            return HttpResponse(str(file))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


          
class ProgramList(ListView):
    model = Program
    def get_queryset(self):
        return Program.objects.filter(instructor=self.request.user)
    
# Delete
# Edit
    
class ProgramBrowse(ListView):
    template_name = 'main_app/program_browser.html'
    model = Program

# def decide_the_userRole(request):
#     profile = Profile.objects.get(user=request.user)
#     context = {'profile': profile}
#     return render(request, 'base.html', context)


def Register_Student_Into_Program(request, program_id):
    student = request.user
    print(student)
    program = Program.objects.get(id = program_id)
    studentProgram = RegisteredStudent(program_id = program, student_id= student)
    studentProgram.save()
    program.seats -= 1
    program.save()        
    return render(request, 'home.html', {'message': 'You joined the class successfully!'})



class My_Programs(ListView):
    template_name = 'main_app/my_programs.html'
    model = RegisteredStudent
    
    def get_context_data(self,**kwargs):
        print("done")
        context=super(My_Programs,self).get_context_data(**kwargs)
        joined_program = RegisteredStudent.objects.filter(student_id_id = self.request.user).values('program_id')
        programs =[]
        for i in joined_program:
            print(i['program_id'])
            p_id = i['program_id']
            programs.append(Program.objects.get(id = p_id ))
        print(programs)      
        context['program_list'] = programs
        return context
    

class student_list(ListView):
    template_name = 'main_app/student_list.html'
    model = RegisteredStudent

    def get_context_data(self,**kwargs):    
    # def student_list(request, program_id):
        print("done")
        # context = super().get_context_data(**kwargs)
        context=super(student_list,self).get_context_data(**kwargs)
        print('pid', kwargs.get('passed_program_id', None))
        print('pid', kwargs(passed_program_id))
        joined_students = RegisteredStudent.objects.filter(program_id_id = kwargs('passed_program_id')).values('student_id')
        print(joined_students)
        students=[]
        for i in joined_students:
            print(i['student_id'])
            s_id = i['student_id']
            students.append(Program.objects.get(id = s_id ))
            print(students)      
            context['student_list'] = students
            return context


  






  
     