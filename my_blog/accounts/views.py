from accounts.models import Login
from django.shortcuts import render
from .serializers import LoginSerializer, UserRegSerializer


# Create your views here.
def home(request):
    return render(request,'accounts/home.html')

def register(request):
    form = UserRegSerializer()
    return render(request,'accounts/register.html',{'form':form})

def login(request):
    form = LoginSerializer()
    return render(request,'accounts/login.html',{'form':form})

