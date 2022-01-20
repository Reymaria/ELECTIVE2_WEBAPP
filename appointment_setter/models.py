from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from datetime import date
from django.db.models import Model
from django.urls import reverse
from django.contrib.auth.models import User

time_choices = [
('8:00 - 9:00 AM', "8:00 - 9:00 AM"),
('9:00 - 10:00 AM', "9:00 - 10:00 AM"),
('10:00 - 11:00 AM', "10:00 - 11:00 AM"),
('2:00 - 3:00 PM', "2:00 - 3:00 PM"),
('3:00 - 4:00 PM', "3:00 - 4:00 PM")
]
status_field_choices = [
    ('PENDING', "PENDING"),
    ('DECLINED', "DECLINED"),
    ('APPROVED', "APPROVED")
]



# Create your models here.
class User_registration (models.Model):
    student_id = models.CharField(max_length= 50, verbose_name= 'student_id') #tupc-id ONLY NUMBERS NEEDED
    surname = models.CharField(max_length= 50, verbose_name= 'surname')
    student_email = models.EmailField(max_length= 200, verbose_name= 'student_email', blank = True)
    student_pass = models.CharField(max_length= 200, verbose_name= 'student_pass')
    class Meta:
        db_table = "user_registration"
    def __str__ (self):
        return self.student_email

class Student_Appointment (models.Model):
    
    student_req_docu = models.CharField(max_length=150, verbose_name= 'student_req_docu')
    req_date = models.CharField(max_length=200, verbose_name= 'req_date')
    req_time_choices = models.CharField(max_length=200, 
    choices = time_choices, blank = True, null = True)
    status_field = models.CharField(max_length=200, verbose_name = "status_field",
    choices = status_field_choices, blank = True, null = True)
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE, null=True)
    date_posted = models.DateField(default=date.today)
    user_name = models.CharField(max_length=200, verbose_name= 'user_name')
    # Student = models.ForeignKey(User_registration, on_delete = models.CASCADE)
    class Meta:
        db_table = "student_appointment"

 
    def __str__ (self):
        return self.student_req_docu