from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from musician.models import Musician
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.utils.decorators import method_decorator

# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('user_login')
        
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form': register_form, 'type': 'register'})

# class SignUp(CreateView):
#     template_name = 'register.html'
#     success_url = reverse_lazy('user_login')
#     form_class = forms.RegistrationForm()
# def user_login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#            user_name = form.cleaned_data['username']
#            user_pass = form.cleaned_data['password']
#            user = authenticate(username = user_name, password=user_pass)
#            if user is not None:
#                messages.success(request, 'Log In Successfully')
#                login(request, user)
#                return redirect('home') 
#            else:
#                 messages.warning(request, 'Login Information Incorrect')
#                 return redirect('user_login')
#         else:
#             messages.warning(request, 'not a valid user')
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#         return render(request, 'register.html', {'form': form, 'type': 'Login'})
    
class UserLogin(LoginView):
    template_name='register.html'
    def get_success_url(self) -> str:
        return reverse_lazy('home')
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in Information Incorrect')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Login' 
        return context

@method_decorator(login_required, name='dispatch')
class LogOut(LogoutView):
    def get_success_url(self):
        return reverse_lazy('user_login')
    