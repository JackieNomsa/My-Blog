from accounts.models import Login
from django.shortcuts import render
from .serializers import LoginSerializer, UserRegSerializer


# Create your views here.
def login(request):
    form = LoginSerializer()
    return render(request,'accounts/login.html',{'form':form})
