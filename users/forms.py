from django import forms
from .models import User


class UserCreateForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserLoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)