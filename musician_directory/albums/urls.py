from django.urls import path
from .views import *
urlpatterns = [
    path('add/',add_album,name='album'),
    path('delete/<int:id>',delete,name='delete'),
    path('edit/<int:id>',edit,name='edit'),
]