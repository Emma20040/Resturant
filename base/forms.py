from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms 
from .models import CustomUser


class LoginForm(UserCreationForm):
    name = forms.CharField()
    email = forms. EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# creating a customer form for users
class CustomerUserForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields =['username', 'email', 'first_name', 'last_name', 'phone_number', 'address', 'password1', 'password2']

# custom form to login user
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email or Username')