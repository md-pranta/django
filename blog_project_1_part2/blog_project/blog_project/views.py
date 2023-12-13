from django.shortcuts import render
from posts.models import Post
from catagories.models import Catagory
def home(req,category_slug=None):
    data = Post.objects.all()
    if category_slug is not None:
        catagory = Catagory.objects.get(slug=category_slug)
        data = Post.objects.filter(catagory=catagory)
    cata = Catagory.objects.all()
    return render(req, 'home.html',{'data':data,'catagory':cata})
