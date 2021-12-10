from django.forms import ModelForm
from .models import User_registration, Student_Appointment
from django import forms

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