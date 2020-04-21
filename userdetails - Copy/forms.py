from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core import validators
import re

class signupForm(forms.Form):
    first_name=forms.CharField(max_length=25)
    last_name=forms.CharField(max_length=25)
    username=forms.CharField(max_length=15)
    email=forms.EmailField()
    password=forms.CharField(max_length=15,widget=forms.PasswordInput(render_value=False))
    confirm_password=forms.CharField(max_length=15,widget=forms.PasswordInput(render_value=False))

    def clean(self):
        total_cleaned_data=super().clean()
        first_name=total_cleaned_data['first_name']
        if len(first_name)<3:
            raise forms.ValidationError('Firstname should be more than 3 letters')
        last_name=total_cleaned_data['last_name']
        username=total_cleaned_data['username']
        if len(username)<3:
            raise forms.ValidationError('username should be more than 3 letters')
        password=total_cleaned_data['password']
        confirm_password=total_cleaned_data['confirm_password']
        if password!=confirm_password:
            raise forms.ValidationError("Both passwords should match")
        elif len(password)<4:
            raise forms.ValidationError("Password should be more than 4 letters")
        
        

    
   
class loginForm(forms.Form):
    username=forms.CharField(max_length=15)
    password=forms.CharField(max_length=15,widget=forms.PasswordInput(render_value=False))
    
   
        

   



    

