from django import forms
from VK.models import UserInfo


class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)

class AvatarForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['avatar']
