from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician
# Create your views here.
def add_musician(req):
    form = MusicianForm()
    if req.method == 'POST':
        form = MusicianForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    return render(req, 'musician.html', {'form':form})

def edit_musician(req, id):
    data = Musician.objects.get(pk=id)
    form = MusicianForm(instance=data)
    if req.method == 'POST':
        form = MusicianForm(req.POST, instance=data)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    return render(req, 'musician.html', {'form':form})