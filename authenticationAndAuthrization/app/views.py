from django.shortcuts import render, redirect
from .forms import RegisterForm,ChangeForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.
def home(req):
    return render(req, 'home.html')



def signup(req):
    if not req.user.is_authenticated:
        form = RegisterForm()
        if req.method == 'POST':
            form = RegisterForm(req.POST)
            if form.is_valid():
                messages.success(req, 'Account created successfully')
                form.save()
                print(form.changed_data)
        return render(req, 'signup.html', {'form': form})
    return redirect('profile')


def userlogin(req):
    if not req.user.is_authenticated:
        form = AuthenticationForm()
        if req.method == 'POST':
            form = AuthenticationForm(request=req, data = req.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username = name, password = user_pass)
                if user is not None:
                    login(req, user)
                    return redirect('profile')
        return render(req, 'login.html', {'form':form})
    return redirect('profile')

def profile(req):
    if req.user.is_authenticated:
        form = ChangeForm(instance=req.user)
        if req.method == 'POST':
            form = ChangeForm(req.POST, instance=req.user)
            if form.is_valid():
                messages.success(req, 'Account updated successfully')
                form.save()
                print(form.changed_data)
        return render(req, 'profile.html', {'form': form})
    return redirect('signup')

def userlogout(req):
    logout(req)
    return redirect('login')


def pass_change(req):
    form  = PasswordChangeForm(user=req.user)
    if req.method == 'POST':
        form  = PasswordChangeForm(user = req.user, data = req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user)
            return redirect('profile')
    return render(req, 'passChange.html', {'form':form})


def pass_change2(req):
    form  = SetPasswordForm(user=req.user)
    if req.method == 'POST':
        form  = SetPasswordForm(user = req.user, data = req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user)
            return redirect('profile')
    return render(req, 'passChange.html', {'form':form})



def change_form(req):
    if req.user.is_authenticated:
        form = ChangeForm()
        if req.method == 'POST':
            form = ChangeForm(req.POST, instance=req.user)
            if form.is_valid():
                messages.success(req, 'Account updated successfully')
                form.save()
                print(form.changed_data)
        return render(req, 'profile.html', {'form': form})
    return redirect('signup')