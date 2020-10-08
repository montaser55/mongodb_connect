from django.shortcuts import render

from django.http import HttpResponse

from .models import Student

# Create your views here.

def home(request):
    student_data= Student.objects.all()
    for field in student_data:
        print("name of student is:", field.name)
    return HttpResponse("See the terminal for result")
 