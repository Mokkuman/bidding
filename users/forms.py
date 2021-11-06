from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('firstName','lastName','email','city','state',)
        widgets = {
        'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'E-mail'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    fields = ['e', 'password']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstName','lastName','city','state',)