from accounts.models import Login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegForm


# Create your views here.
def home(request):
    return render(request,'accounts/home.html')

def register(request):
    if request.method == 'POST':
        context = {}
        form = UserRegForm(request.POST)
        if form.is_valid():
            u_name = form.cleaned_data['username']
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            pass_word = form.cleaned_data['password']
            
            user = User.objects.create_user(username=u_name,first_name=f_name,last_name=l_name,email=email,password=pass_word)

            user.save()
            
            header='User Created, You can login to your account'
                
            
            print('registered')

        return redirect('login',{'context':header})
    
    form = UserRegForm()
    return render(request,'accounts/register.html',{'form':form})

def login(request,**kwargs):
    form = LoginForm()
    return render(request,'accounts/login.html',{'form':form})

users = User.objects.all()
print(users)

