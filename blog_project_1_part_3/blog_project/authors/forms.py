from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class AuthorFrom(forms.ModelForm):
#     class Meta:
#         model = Author
        
#         fields = '__all__'

class RegisterForm(UserCreationForm):
    password = None
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    
    class Meta:
        model = User
        
        fields = ['username', 'first_name', 'last_name', 'email']

class ChangeUserData(UserChangeForm):
    class Meta:
        model = User
        
        fields = ['username', 'first_name', 'last_name', 'email']