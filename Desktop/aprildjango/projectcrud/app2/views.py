from django.shortcuts import render
from django.http import HttpResponse
from app2.models import Student
# Create your views here.
def home(request):
    return render (request,"app2/home.html")
def about(request):
    student_data = Student.objects.all()
    #student_data = Student.objects.all()
    return render (request,"app2/about.html",{'students':student_data})
