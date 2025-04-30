from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms 

# forms to register new users
class Register(UserCreationForm):
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    address= forms.CharField()

    class Meta:
        model = User
        fields = ['name', 'email', 'phone_number', 'address', 'username']

class LoginForm(UserCreationForm):
    name = forms.CharField()
    email = forms. EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password']
