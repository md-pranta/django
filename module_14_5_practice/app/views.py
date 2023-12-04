from django.shortcuts import render
from .forms import *
# Create your views here.
def home(req):
    form = Practice()
    if req.method == 'POST':
        form = Practice(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
    return render(req, 'home.html',{'form':form})