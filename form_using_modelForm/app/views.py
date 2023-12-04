from django.shortcuts import render
from .forms import *

# Create your views here.
def home(req):
    form = StudentForm()
    if req.method == 'POST':
        form = StudentForm(req.POST)
        if form.is_valid():
            form.save()
            print(form.changed_data)
    return render(req, 'home.html', {'form':form})