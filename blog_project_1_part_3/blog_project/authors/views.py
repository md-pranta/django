from django.shortcuts import render, redirect
from .forms import RegisterForm, ChangeUserData
from posts.models import Post
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.
# def add_author(req):
#     author_form = AuthorFrom()
#     if req.method == 'POST':
#         author_form = AuthorFrom(req.POST)
#         if author_form.is_valid():
#             # print(author_form.cleaned_data)
#             author_form.save()
#             return redirect('add_author')
#     return render(req, 'add_author.html',{'form': author_form})

def signUp(req):
    signup = RegisterForm()
    if req.method == 'POST':
        signup = RegisterForm(req.POST)
        if signup.is_valid():
            signup.save()
            messages.success(req, 'account create successfully')
            return redirect('signup')
    return render(req, 'signup.html',{'form': signup, 'type': 'signup'})

def user_login(req):
    form = AuthenticationForm
    if req.method == 'POST':
        form = AuthenticationForm(req, req.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(req, 'Login successfully')
                login(req, user)
                return redirect('profile')
            messages.warning(req, 'login information incorrect')
            return redirect('signup')
    return render(req, 'signup.html', {'form':form,'type':'login'})

#class base view
class UserLoginVieew(LoginView):
    template_name = 'signup.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'login successfull')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'login information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login' 
        return context
    
    
    




@login_required
def profile(req):
    data = Post.objects.filter(author=req.user)
    return render(req, 'profile.html', {'data':data})
@login_required
def edit(req):
    profile = ChangeUserData(instance=req.user)
    if req.method == 'POST':
        profile = ChangeUserData(req.POST, instance=req.user)
        if profile.is_valid():
            profile.save()
            messages.success(req, 'Profile Upadated successfully')
            return redirect('profile')
    return render(req, 'update_profile.html',{'form': profile})

@login_required
def pass_change(req):
    pas = PasswordChangeForm(user=req.user)
    if req.method == 'POST':
        pas = PasswordChangeForm(req.user,data = req.POST)
        if pas.is_valid():
            pas.save()
            messages.success(req, 'updated password successfully')
            update_session_auth_hash(req, pas.user)
            return redirect('home')
    return render(req, 'change_pass.html',{'form': pas})


@login_required
def log(req):
    logout(req)
    return redirect('login')

#class base logout
class Logout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')