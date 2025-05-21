from django import forms
from  .models import Food

class UploadLoadFood(forms.ModelForm):

    class Meta:
        model = Food
        fields = ['name', 'price', 'image', 'category']