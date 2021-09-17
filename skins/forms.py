from django import forms
from .models import Skin


class SkinCreateForm(forms.ModelForm):

    SKIN_TYPE_CHOICES = (
        ('1', 'Low res'),
        ('2', 'High res')
    )

    name = forms.CharField(required=True)
    description = forms.CharField(required=False)
    skin_type = forms.ChoiceField(choices=SKIN_TYPE_CHOICES)

    skin_id = forms.CharField(required=True)

    class Meta:
        model = Skin
        fields = ('name', 'description', 'skin_type', 'image')
