from django.db.models import fields
from django.forms import ModelForm
from .models import Student_Appointment
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from appointment_setter import models


class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2' ]

class StudentAppointmentForm (ModelForm):
    # student_req_docu = forms.CharField(#verbose_name= 'student_req_docu',
    #                                     # widget = forms.TextInput(attrs{'style': 'text-transform:uppercase', 'id': 'student_requested_docu', 'name': 'student_requested_docu' ,'placeholder': 'e.g. COR'})
    #                                   )

    class Meta:
        model = Student_Appointment
        fields =  ("student_req_docu", "req_date", "req_time_choices", "status_field")
        labels = {
            'student_req_docu': 'REQUESTED DOCUMENT',
            'req_date': 'DATE REQUESTED',
            'req_time_choices': 'TIME REQUESTED',
        }
        widgets = {
            'student_req_docu': forms.TextInput(attrs = {'style': 'text-transform:uppercase', 'id': 'student_requested_docu', 'name': 'student_requested_docu' ,'placeholder': 'e.g. COR'}),
            'req_date': forms.TextInput(attrs = {'style': 'cursor: pointer;', 'id': 'date', 'placeholder': 'mm/dd/yy', 'name': 'req_date', 'readonly':'readonly', 'required': 'required'}),
            'status_field':forms.TextInput(attrs={'type':'hidden'}),
            # 'status_field':forms.TextInput(attrs={'value':'PENDING'}),
            'req_time_choices': forms.Select(attrs = {'id': 'time','required':'required'}),

        }

class AdminUpdate(ModelForm):
    class Meta:
        model = Student_Appointment
        fields =  ("user_field","student_req_docu", "req_date", "req_time_choices", "status_field")
        labels = {
            'user_field': 'STUDENT ID',
            'student_req_docu': 'REQUESTED DOCUMENT',
            'req_date': 'DATE REQUESTED',
            'req_time_choices': 'TIME REQUESTED',
            'status_field': 'APPOINTMENT STATUS'
        }
        widgets = {
            'user_field': forms.TextInput(attrs = {'style': 'cursor: pointer;', 'name': 'user_field', 'readonly':'readonly'}),
            'student_req_docu': forms.TextInput(attrs = {'style': 'text-transform:uppercase', 'id': 'student_requested_docu', 'name': 'student_requested_docu' ,'placeholder': 'e.g. COR', 'readonly':'readonly'}),
            'req_date': forms.TextInput(attrs = {'style': 'cursor: pointer;', 'id': 'date', 'placeholder': 'mm/dd/yy', 'name': 'req_date','readonly':'readonly'}),
            'req_time_choices': forms.Select(attrs = {'id': 'time','class':'identity', 'required':'required'}),
            'status_field':forms.Select(attrs={'class':'identity'}),
        }
