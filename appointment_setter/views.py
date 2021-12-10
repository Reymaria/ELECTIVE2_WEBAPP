from django.shortcuts import render

# Create your views here.

def home (request):

    return render(request, 'admin/home.html', context)

def about (request):
    return render(request, 'admin/form_modification.html')

def calendar (request):
    return render(request, 'admin/calendar-admin.html')

def loginAndSignUp(request):
    return render(request, 'loginAndSignup/index.html')

def StudentSideHome(request):
    return render(request, 'student_side/home.html')