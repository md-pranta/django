from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('register/', views.CreateView.as_view(), name='register'),
    path('login/', views.UserLogin.as_view(), name='user_login'),
    path('logout/', views.LogOut.as_view(), name='user_logout'),
    # path('logout/',LogoutView.as_view(), name='user_logout'),
    
]
