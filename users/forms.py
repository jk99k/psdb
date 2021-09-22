from django import forms
from django.core.exceptions import ValidationError
from .models import User


class UserCreateForm(forms.ModelForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Password', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserEditForm(forms.ModelForm):

    CLIENT_CHOICES = [
        ('1', 'Smart Phone'),
        ('2', 'Tablet'),
        ('3', 'PC')
    ]

    username = forms.CharField(required=False)
    profile = forms.CharField(required=False)
    client = forms.ChoiceField(choices=CLIENT_CHOICES ,required=False)
    icon = forms.ImageField(required=False)
    pixel_strike_id = forms.IntegerField(required=False)
    when_started = forms.IntegerField(required=False)
    youtube_channel = forms.CharField(required=False)
    tiktok_account = forms.CharField(required=False)
    discord_account = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'profile', 'client',  'icon', 'pixel_strike_id', 'when_started', 'youtube_channel', 'tiktok_account', 'discord_account')