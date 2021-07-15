from django.db import models
from django.contrib.auth import User

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_info = models.ForeignKey(User,on_delete=models.CASCADE)