from django.urls import path
from .views import *
urlpatterns = [
    # path('add/',add_post,name='add_post'),
    path('add/',AddcreateView.as_view(),name='add_post'),
    # path('edit/<int:id>',edit_post,name='edit_post'),
    path('edit/<int:id>',EditPostView.as_view(),name='edit_post'),
    # path('delete/<int:id>',delete_post,name='delete_post'),
    path('delete/<int:id>',DeletePostView.as_view(),name='delete_post'),
    path('detail_post/<int:id>',Details.as_view(),name='detail_post'),
]