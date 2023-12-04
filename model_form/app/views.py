from django.shortcuts import render
from .models import *
# Create your views here.
def home(req):
    student = Student.objects.all()
    # print(Student)
    return render(req, 'home.html', {'data':student})