from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *



class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('__all__')
        exclude = ['user']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)





class UserForm(UserCreationForm):
    username=forms.CharField(label='Your Name',widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Name'}))
    email=forms.EmailField(label='Your Email',widget=forms.EmailInput(attrs={'class':'form-control','placeholder': 'email@gmail.com'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'Password'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder': 'confirm Password'}))

    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']


class SignInForm(forms.Form):
    username=forms.CharField(label='Your Username',widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))

from django import forms

