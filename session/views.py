from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from cart.models import Cart
from django.utils.timezone import datetime
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('all-product')
        else:
            messages.error(request,'Invalid username or password')
    return render(request,'login.html')

def Logout(request):
    logout(request)
    return redirect('login')

def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            user = User.objects.get(username = username)
            new_cart = Cart.objects.create(user = user,created_at = datetime.now())
            new_cart.save()
            messages.success(request,'Account creation successfull,please login')
            logout(request)
            return redirect('login')
        else:
            messages.error(request,'Something went wrong')
    else:
        form = CustomUserCreationForm()
    return render(request,'signup.html',{'form':form})   

@login_required(login_url = 'login')
def ChangePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user = user)
            messages.success(request,'Successfully change your password')
            return redirect('home')
        else:
            messages.error(request,f'OOPS!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request,'changepassword.html',{'form':form})
    




        



