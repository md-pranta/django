from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('delete/<int:roll>', delete, name="delete"),
]