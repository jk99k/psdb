from django import forms
from .models import Skin


class SkinCreateForm(forms.ModelForm):

    SKIN_TYPE_CHOICES = (
        ('1', 'Low res'),
        ('2', 'High res')
    )

    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Skin name'}))
    description = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    skin_type = forms.ChoiceField(choices=SKIN_TYPE_CHOICES)
    motif = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Motif'}))

    skin_id = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Skin ID'}))

    class Meta:
        model = Skin
        fields = ('name', 'description', 'skin_type', 'image', 'motif', 'skin_id')