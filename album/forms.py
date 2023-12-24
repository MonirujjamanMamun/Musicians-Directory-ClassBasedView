from django import forms
from .models import Album


class AddAlbumForms(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
