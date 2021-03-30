from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import UserInfo

class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = ('user',)