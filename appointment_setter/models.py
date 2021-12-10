from django.db import models
from django.utils import timezone
from datetime import date
from django.db.models import Model
from django.urls import reverse

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
