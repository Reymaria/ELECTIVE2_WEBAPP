from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from appointment_setter.models import User_registration
from appointment_setter.models import Student_Appointment, User
from django.contrib import messages
from .models import Student_Appointment
from .forms import StudentAppointmentForm
from .forms import UserRegisterForm
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *



# Create your views here.
def user_register (request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.user = request.user;
            obj.user.is_staff = True
            obj.user.is_active = False
            obj.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'ACCOUNT SUCCESSFULLY CREATED for {username}!')
            print('I am working!')
            return redirect ('/')
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)

@unauthorized_user
def user_login_interface (request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None and user.is_superuser:
            # if username == 'admin' and password == "elective2":
            print("I am staff")
            login(request, user,  backend='django.contrib.auth.backends.ModelBackend')
            # message = "welcome admin"
            messages.add_message(request, messages.SUCCESS,
                                    f'Welcome Admin {username}!')
            
            return redirect ('admin/')
            
        elif user is not None and user.is_active:
            print("I am student")
            login(request, user)
            # message = "welcome user"
            messages.add_message(request, messages.SUCCESS,
                                    f'welcome student')

            return redirect ('student/')
        else:
            # message = "invalid credentials"
            messages.add_message(request, messages.ERROR,
                                f'INVALID CREDENTIALS for {username}. Incorect username or password')
            
            return render(request, 'users/login.html' )

    return render(request, 'users/login.html')

@login_required
def CreateUser(request):

    if request.method == "POST":
        if  request.POST.get('surname') and request.POST.get('student_id') and request.POST.get('student_email') and request.POST.get('student_pass'):
            saverecord = User_registration()
            saverecord.surname = request.POST.get('surname')
            saverecord.student_id = request.POST.get('student_id')
            saverecord.student_email = request.POST.get('student_email')
            saverecord.student_pass = request.POST.get('student_pass')
            saverecord.save()
            messages.success(request, "Account Successfuly created ....!")
            return render (request, 'loginAndSignup/index.html')

    else:
        messages.error(request, 'Problem occured, please try again!')
        return render (request, 'loginAndSignup/index.html')
     

@login_required
def ScheduleAppointment(request):
    # initial_data = {
    #     'status_field': 'pending'
    # }
    form = StudentAppointmentForm
    if request.method == "POST":
        # appointments[]
        form = StudentAppointmentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect ('student/schedule-appointment/')
    # else:
    #     form = StudentAppointmentForm
    return render(request, 'student_side/home.html', {'form':form})

@login_required
def home (request):
    readAppointment = Student_Appointment.objects.all()
    content = {'readAppointment': readAppointment}
    return render(request, 'admins/home.html', content )
    
@login_required
def about (request, data_id):
    data = Student_Appointment.objects.get(id=data_id)

    form = AdminUpdate(instance=data)
    if request.method == "POST":
        form = AdminUpdate(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/admin/')
    # content = {'datas':datas, 'form':form}
    content = {'form':form}

    return render(request, 'admin/form_modification.html', content)
@login_required
def calendar (request):
    return render(request, 'admin/calendar-admin.html')
@login_required
def loginAndSignUp(request):
    return render(request, 'loginAndSignup/index.html')
@login_required
def StudentSideHome(request):
    form = StudentAppointmentForm(initial = {'status_field': 'PENDING'})
    readAppointment = Student_Appointment.objects.all()
    if request.method == "POST":
        form = StudentAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    return render(request, 'student_side/home.html', {'readAppointment': readAppointment, 'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, ("You were Log out, please Log in again"))
    return redirect('/')

def redirection (request):
    readAppointment = Student_Appointment.objects.all()
    return render(request, 'student_side/redirection.html', {'readappointment':readAppointment})