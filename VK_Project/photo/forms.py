from django import forms
from photo.models import Picture


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['picture']