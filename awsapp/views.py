from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .emails import otp_send
from django.contrib.auth.models import User

# otp_send('yogishaeveeru@gmail.com')


# Create your views here.
def index(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.info(request,'Username or Password invalid')   
    return render(request,'login.html',{})

# def regist(request):
#     form=CreateUserForm()
#     if request.method=='POST':
#         form=CreateUserForm(request.POST)
#         if form.is_valid():
#             email=request.POST.get('email')
#             d=email.split('@')
#             if d[1]=='gmail.com':
#                 form.save()
#                 messages.success(request,'Registration successful')
#                 return redirect('login')
#             else:
#                 messages.info(request,'Use company Email')
#     context={'form':form}
#     return render(request,'registration.html',context)
def home(request):
    return render(request,'base.html')

@login_required(login_url='login')
def profile(request):
    return render(request,'profile.html',{"user":request.user})

def log_out(request):
    logout(request)
    return redirect('login')
firstname=''
lastname=''
email=''
otp=''
def regdisp(request):
    return render(request,'registration.html',{})
def regist(request):
    global firstname,lastname,email,otp
    # form=CreateUserForm()
    if request.method=='POST':
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        otp=otp_send(email)
        return render(request,'next.html',{'email':email})
    else:
        return redirect('regdisp')


def verifyotp(request):
    userotp=request.POST.get('otpverif')
    if int(userotp)==otp:
        return render(request,'password.html',{})
    else:
        messages.info(request,'Invalid otp')
        return render(request,'next.html',{})

def userRegister(request):
    if request.method=='POST':
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            user=User(first_name=firstname,last_name=lastname,email=email,password=password1,username=email,is_staff=True)
            user.save()
            messages.success(request,'Registration successful')
            return redirect('login')
        else:
            messages.info(request,'Password didnot match')
            return render(request,'password.html',{})


