from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
# Create your views here.

@method_decorator(login_required, name='dispatch')
class Add_Album(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditPost(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    pk_url_kwarg ='id'
    success_url=reverse_lazy('home')

@method_decorator(login_required, name='dispatch')
class Delete_Album(DeleteView):
    model = models.Album
    template_name = 'delete_album.html'
    success_url=reverse_lazy('home')
    pk_url_kwarg='id'