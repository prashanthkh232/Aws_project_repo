from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.info(request,'Username or Password invalid')   
    return render(request,'login.html',{})

def regist(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            email=request.POST.get('email')
            d=email.split('@')
            if d[1]=='gmail.com':
                form.save()
                messages.success(request,'Registration successful')
                return redirect('login')
            else:
                messages.info(request,'Use company Email')
    context={'form':form}
    return render(request,'registration.html',context)
def home(request):
    return render(request,'base.html')

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html',{"user":request.user})

def log_out(request):
    logout(request)
    return redirect('login')