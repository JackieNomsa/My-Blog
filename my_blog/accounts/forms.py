from django import forms

from rest_framework import serializers
from .models import Login, User

class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Login
        fields = ['username','password']

class UserRegForm(forms.Form):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']