from django.urls import path
from .views import *
urlpatterns = [
    path('add/',add_musician,name='musician'),
    path('edit/<int:id>',edit_musician,name='edit_musician'),
]