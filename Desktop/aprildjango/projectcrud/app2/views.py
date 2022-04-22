from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render (request,"app2/home.html")
def about(request):
    return HttpResponse("class , age, details,rollno ")
