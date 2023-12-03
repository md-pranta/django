from django.shortcuts import render
from .forms import *
# Create your views here.
def home(req):
    return render(req, 'home.html')
    
def about(req):
    if req.method == 'POST':
        name = req.POST.get('username')
        email = req.POST.get('email')
        select = req.POST.get('select')
        return render(req, 'about.html',{'name':name,'email':email,'select':select})
    return render(req, 'about.html')

def submit_form(req):
    return render(req, 'forms.html')

def djangoForm(req):
    if req.method == 'POST':
        form = contactForm(req.POST, req.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./app1/upload/' + file.name, 'wb+') as destinaton:
            #     for chunk in file.chunks():
            #         destinaton.write(chunk)
            print(form.cleaned_data)
    else:
        form = contactForm()
    return render(req, 'django_form.html', {'form':form})

def studentForm(req):
    form = StudentData()
    if req.method == 'POST':
        form = StudentData(req.POST, req.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(req, 'django_form.html',{'form':form})
    return render(req, 'django_form.html',{'form':form})
def passValidation(req):
    form = passwordValidation()
    if req.method == 'POST':
        form = passwordValidation(req.POST, req.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            return render(req, 'django_form.html',{'form':form})
    return render(req, 'django_form.html',{'form':form})
        