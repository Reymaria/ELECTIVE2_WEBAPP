from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.home, name = 'admin-home'), 
    # path('home/', views.home, name = 'Admin-home'), #admin/home
    path('admin/about/<data_id>/', views.about, name = 'admin-about'),
    path('', views.loginAndSignUp, name = 'main-home'), 
    path("registration/", views.CreateUser, name= "create-user"),
    path('student/', views.StudentSideHome, name = 'dashboard-home'), 
    path("student/schedule-appointment/", views.ScheduleAppointment, name= "schedule-appointment"),
]
