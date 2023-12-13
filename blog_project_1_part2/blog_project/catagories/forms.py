from django import forms

from .models import Catagory


class CatagoryFrom(forms.ModelForm):
    class Meta:
        model = Catagory
        
        fields = '__all__'