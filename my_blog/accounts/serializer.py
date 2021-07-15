from django import forms

from rest_framework import serializers
from .models import Login, User

class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(widget=serializers.PasswordInput)
    class Meta:
        model = Login
        fields = ['username','password']

class UserRegSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']