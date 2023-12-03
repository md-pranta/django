from typing import Any
from django import forms
from django.core import validators


class contactForm(forms.Form):
    name = forms.CharField(label='User Name',help_text='total length', required=False,disabled=False, widget=forms.Textarea(attrs={'id':'textArea' ,'class':'class1' ,'placeholder': 'enter your name'}))
    # file = forms.FileField()
    # email = forms.EmailField(label='Email')
    # age  = forms.IntegerField()
    # weight = forms.FloatField()
    # balance = forms.DecimalField()
    # check = forms.BooleanField()
    date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    appointment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    choice = [('s', 'small'),('m', 'medium'),('l', 'large')]
    size = forms.ChoiceField(choices=choice,widget=forms.RadioSelect)
    meal =  [('s', 'small'),('m', 'medium'),('l', 'large')]
    pizza = forms.MultipleChoiceField(choices=meal, widget=forms.CheckboxSelectMultiple)
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     # def clean_name(self):
#     #     valname = self.cleaned_data["name"]
#     #     if len(valname) < 10:
#     #         raise forms.ValidationError("at least 10 character")
#     #     return valname
#     # def clean_email(self):
#     #     data = self.cleaned_data["email"]
#     #     if '.com' not in data:
#     #         raise forms.ValidationError('must contain: .com')
#     #     return data
    
#     def clean(self):
#         cleaned_data = super().clean()
#         name = self.cleaned_data['name']
#         email = self.cleaned_data['email']
        
#         if len(name) < 10:
#             raise forms.ValidationError("at least 10 character")
        
#         if '.com' not in email:
#             raise forms.ValidationError('must contain: .com')

class StudentData(forms.Form):
    name = forms.CharField(widget=forms.TextInput, validators=[validators.MinLengthValidator(8)])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator()])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(35), validators.MinValueValidator(23)])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['png'])])

class passwordValidation(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        pas = self.cleaned_data['password']
        cpas = self.cleaned_data['confirm_password']
        name = self.cleaned_data['name']
        
        if len(name) < 8:
            raise forms.ValidationError(message='name')
        
        if pas != cpas:
            raise forms.ValidationError(message='pass')
    
    # def clean_name(self):
    #     data = self.cleaned_data["name"]
    #     if len(data)<8:
    #         raise forms.ValidationError('name')
    #     return data
    # def clean_pass(self):
    #     data = self.cleaned_data["pass"]
    #     if self.password != self.confirm_password:
    #         raise forms.ValidationError(message='password') 
    #     return data