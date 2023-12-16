from django.shortcuts import render, redirect
from . import forms
from .import models 
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class add_musician(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')
    
    def form_valid(self, form):
        form.instance.users = self.request.user
        return super().form_valid(form)
    



@method_decorator(login_required, name='dispatch')
class Edit_Post(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    pk_url_kwarg ='id'
    success_url = reverse_lazy('home')