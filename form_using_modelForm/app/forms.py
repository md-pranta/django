from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        
        fields = '__all__'
        # fields = ['name', 'roll']
        
        # exclude = ['name', 'address']
        
        labels = {
            'name':'Student name',
        }
        
        widgets = {
            'name':forms.TextInput()
        }
        
        help_texts = {
            'name' : 'write your full name'
        }
        
        error_messages = {
            'name' : {'required':'your name is required'}
        }