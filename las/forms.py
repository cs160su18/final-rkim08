from django.contrib.auth.models import User
from django import forms
from .models import *

class UserForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)
  
  class Meta:
    model = User
    fields = ['username', 'password', 'first_name', 'last_name']
    
class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['title', 'company', 'field']