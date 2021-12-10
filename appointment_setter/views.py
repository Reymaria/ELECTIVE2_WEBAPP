from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from appointment_setter.models import User_registration
from appointment_setter.models import Student_Appointment
from django.contrib import messages
from .models import Student_Appointment
from .forms import StudentAppointmentForm
from .forms import *


# Create your views here.

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


def home (request):
    readAppointment = Student_Appointment.objects.all()
    content = {'readAppointment': readAppointment}
    return render(request, 'admin/home.html', content )

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

def calendar (request):
    return render(request, 'admin/calendar-admin.html')

def loginAndSignUp(request):
    return render(request, 'loginAndSignup/index.html')

def StudentSideHome(request):
    form = StudentAppointmentForm(initial = {'status_field': 'PENDING'})
    readAppointment = Student_Appointment.objects.all()
    if request.method == "POST":
        form = StudentAppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.path)
    return render(request, 'student_side/home.html', {'readAppointment': readAppointment, 'form':form})
