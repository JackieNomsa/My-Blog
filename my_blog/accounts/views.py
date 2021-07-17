from accounts.models import Login
from django.shortcuts import render
from .serializers import LoginSerializer, UserRegSerializer


# Create your views here.
def register(request):
    form = UserRegSerializer()
    return render(request,'accounts/register.html',{'form':form})
