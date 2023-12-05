from django.shortcuts import render
from posts.models import Post
def home(req):
    data = Post.objects.all()
    return render(req, 'home.html',{'data':data})
