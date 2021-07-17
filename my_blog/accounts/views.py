from accounts.models import Login
from django.shortcuts import render
from .forms import LoginForm, UserRegForm


# Create your views here.
def home(request):
    return render(request,'accounts/home.html')

def register(request):
    form = UserRegForm()
    return render(request,'accounts/register.html',{'form':form})

def login(request):
    form = LoginForm()
    return render(request,'accounts/login.html',{'form':form})

