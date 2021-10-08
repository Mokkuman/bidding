from django import forms
from django.forms import ModelForm, fields
from store.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
        'password': forms.PasswordInput(),
        }
