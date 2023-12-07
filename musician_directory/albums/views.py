from django.shortcuts import render, redirect
from .forms import AlbumForm
from musicians.models import Musician
from .models import Album
# Create your views here.
def add_album(req):
    form = AlbumForm()
    if req.method == 'POST':
        form = AlbumForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    return render(req, 'album.html', {'form':form})
def edit(req, id):
    data = Album.objects.get(pk = id)
    form  = AlbumForm(instance=data)
    if req.method == 'POST':
        form = AlbumForm(req.POST, instance=data)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('home')
    return render(req, 'album.html', {'form':form})

def delete(req, id):
    data = Musician.objects.get(pk=id)
    data.delete()
    return redirect('home')