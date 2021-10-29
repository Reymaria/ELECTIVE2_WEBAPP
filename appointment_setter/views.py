from django.shortcuts import render

#ITO ANG ADMIN SIDE NG APPOINTMENT SETTER
posts = [
    {
        'StudentName': 'TUPC-18-0127',
        'ReqDocu': 'ID Verification',
        'request_date': "October 29, 2021",
        'request_time': "8:00 - 9:00 AM"

    },
    {
        'StudentName': 'TUPC-19-0227',
        'ReqDocu': 'Certificate of Registration',
        'request_date': "October 10, 2021",
        'request_time': "9:00 - 10:00 AM"

        
    },
    {
        'StudentName': 'TUPC-16-0129',
        'ReqDocu': 'TOR',
        'request_date': "November 5, 2021",
        'request_time': "2:00 - 3:00 PM"


    },
    {
        'StudentName': 'TUPC-21-0148',
        'ReqDocu': 'ID Verification',
        'request_date': "November 4, 2021",
        'request_time': "8:00 - 9:00 AM"

    }
]
# Create your views here.

def home (request):
    context = {
        'posts': posts
    }
    
    return render(request, 'admin/home.html', context)

def about (request):
    return render(request, 'admin/form_modification.html')

def calendar (request):
    return render(request, 'admin/calendar-admin.html')

def loginAndSignUp(request):
    return render(request, 'loginAndSignup/index.html')

def StudentSideHome(request):
    return render(request, 'student_side/home.html')