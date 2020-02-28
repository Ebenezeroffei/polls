from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class NewUserForm(UserCreationForm):
    first_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {
        'class':'form-control',
    }));
    last_name = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {
        'class':'form-control',
    }));
    
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