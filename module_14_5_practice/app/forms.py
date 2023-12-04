from django import forms
from django.forms.widgets import NumberInput


class Practice(forms.Form):
    name = forms.CharField(max_length=20,min_length=5, label='plz enter your name')
    comment1 = forms.CharField(widget=forms.Textarea())
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(initial='your email')
    agree = forms.BooleanField()
    date = forms.DateField()
    birthYear = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    
    Birth_cho = ['2021', '2022', '2023']
    
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years = Birth_cho))
    
    number = forms.DecimalField(required=False)
    
    choice = [('s', 'small'),('m', 'medium'),('l', 'large')]
    size = forms.ChoiceField(choices=choice)
    
    multiple_choice = forms.MultipleChoiceField(choices=choice, widget=forms.CheckboxSelectMultiple)
    