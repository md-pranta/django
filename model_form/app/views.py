from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def home(req):
    student = Student.objects.all()
    # print(Student)
    return render(req, 'home.html', {'data':student})
    
def delete(req, roll):
    sde = Student.objects.get(pk = roll).delete()
    # print(sde)
    return redirect("home")