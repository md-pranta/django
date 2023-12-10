from django.urls import path, include
from .views import *
urlpatterns = [
    path('',home, name='home'),
    path('signup/',signup, name='signup'),
    path('profile/',profile, name='profile'),
    path('login/',userlogin, name='login'),
    path('logout/',userlogout, name='logout'),
    path('passchange/',pass_change, name='passchange'),
    path('passchange2/',pass_change2, name='passchange2'),
]