from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name = "home"),
    path('about/', about, name = "about"),
    path('form/',submit_form, name='form'),
    path('django_form/',passValidation, name='django_form'),
    
]