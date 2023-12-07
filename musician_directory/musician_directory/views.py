from django.shortcuts import render
from albums.models import Album
def home(req):
    data1 = Album.objects.all()
    return render(req, 'home.html', {'album':data1})