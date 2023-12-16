from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms


class RegisterForm(UserCreationForm):
  first_name = forms.CharField(max_length=50, required=True)
  last_name = forms.CharField(max_length=50, required=True)
  email = forms.EmailField(required=True)
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']

class ProfileChangeForm(UserChangeForm):
  password = None
  class Meta:
    model = User
    fields = ['first_name', 'last_name', 'username', 'email']
