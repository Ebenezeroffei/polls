from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1']
        widgets  = {
            'username': forms.TextInput(attrs = {
                    'class':'form-control',
                }),
            'email': forms.TextInput(attrs = {
                    'class':'form-control',
                    'type':'email',
                    'required':'true',
                }),
            
        }