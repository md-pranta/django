from django.urls import path
from . import views

urlpatterns = [
    # path('', views.add_album, name='add_album'),
    path('', views.Add_Album.as_view(), name='add_album'),
    # path('edit/<int:id>', views.edit_album, name='edit_album'),
    path('edit/<int:id>', views.EditPost.as_view(), name='edit_album'),
    path('delete/<int:id>', views.Delete_Album.as_view(), name='delete_album'),
]