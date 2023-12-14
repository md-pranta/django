from django.urls import path
from .views import *
urlpatterns = [
    path('signup/',signUp,name='signup'),
    # path('login/',user_login,name='login'),
    path('login/',UserLoginVieew.as_view(),name='login'),
    path('profile/',profile,name='profile'),
    path('profile/edit',edit,name='edit'),
    # path('logout/',log,name='logout'),
    path('logout/',Logout.as_view(),name='logout'),
    path('profile/edit/pass_change',pass_change,name='password'),
]