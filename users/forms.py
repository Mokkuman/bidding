from django import forms
from django.forms import ModelForm, fields
#from users.models import User
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstName','lastName','email','password','city','state',)
        widgets = {
        'password': forms.PasswordInput(),
        }
   