from django import forms
from .models import *
from django.forms.widgets import ClearableFileInput

class ImgsForm(forms.ModelForm):
    ID_Type = forms.ModelChoiceField(queryset=ImageType.objects.all(), required=False)
    
    class Meta:
        model = Imgs
        fields = ['ID_Type', 'pic', 'new_img', 'image_url']
    pic = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))