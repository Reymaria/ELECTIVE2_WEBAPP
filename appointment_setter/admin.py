from django.contrib import admin

# Register your models here.

from .models import User_registration
from .models import Student_Appointment

admin.site.register(User_registration)
admin.site.register(Student_Appointment)

