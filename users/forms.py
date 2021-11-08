from django import forms
from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from .models import User
from store.models import BidProduct

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
    fields = ['email', 'password']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('firstName','lastName','city','state','profilePic',)

class UpdateMoneyForm(forms.ModelForm):
    money = forms.IntegerField(widget=forms.NumberInput(None),min_value=0,initial=0,error_messages={0:"Los créditos deben ser mayor o igual a 1"})
    class Meta:
        model = User
        fields = ['money']
