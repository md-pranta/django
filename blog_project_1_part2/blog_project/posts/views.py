from django.shortcuts import render, redirect
from .forms import PostFrom
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_post(req):
    post_form = PostFrom()
    if req.method == 'POST':
        post_form = PostFrom(req.POST)
        if post_form.is_valid():
            post_form.instance.author = req.user
            # print(post_form.cleaned_data)
            post_form.save()
            return redirect('home')
    return render(req, 'add_post.html',{'form': post_form})
@login_required
def edit_post(req, id):
    post = Post.objects.get(pk=id)
    post_form = PostFrom(instance=post)
    if req.method == 'POST':
        post_form = PostFrom(req.POST, instance=post)
        if post_form.is_valid():
            # print(post_form.cleaned_data)
            post_form.save()
            return redirect('home')
    return render(req, 'add_post.html',{'form': post_form})
@login_required
def delete_post(req, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')