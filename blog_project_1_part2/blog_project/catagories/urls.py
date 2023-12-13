from django.urls import path
from .views import *
urlpatterns = [
    path('add/',add_catagory,name='add_catagory'),
]