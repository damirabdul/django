from django import forms
from twitterapp.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = Profile