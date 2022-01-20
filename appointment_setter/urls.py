from django.contrib import auth
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', views.home, name = 'admin-home'), 
    # path('home/', views.home, name = 'Admin-home'), #admin/home
    path('admin/about/<data_id>/', views.about, name = 'admin-about'),
    path('register/', views.loginAndSignUp, name = 'main-home'), 
    path('', views.user_login_interface, name= 'user-log-in-interface' ),    
    path("registration/", views.CreateUser, name= "create-user"),
    path('student/', views.StudentSideHome, name = 'dashboard-home'), 
    path("student/schedule-appointment/", views.ScheduleAppointment, name= "schedule-appointment"),
    path ('user-registration/', views.user_register, name= 'user-registration'),
    path('redirection/', views.redirection, name= 'redirection' ),
    path('logout_user/', views.logout_user, name= 'logout_user' ),
]
