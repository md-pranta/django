from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import PostFrom, CommentFrom
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView,DetailView
from django.utils.decorators import method_decorator
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
#addPost using class based views
@method_decorator(login_required, name='dispatch')
class AddcreateView(CreateView):
    model = Post
    form_class = PostFrom
    template_name = 'add_post.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    



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

#addPost using class based views
@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = Post
    form_class = PostFrom
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    
    success_url = reverse_lazy('profile')
    
#addPost using class based views
@login_required
def delete_post(req, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('home')

@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'


class Details(DetailView):
    model = Post
    pk_url_kwarg = 'id'
    template_name = 'post_detail.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentFrom(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        
        comment_form = CommentFrom()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
        