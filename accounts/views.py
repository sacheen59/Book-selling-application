from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"User register successfully")
            return redirect("/accounts/login/")
        else:
            messages.add_message(request,messages.ERROR,"User register failed")
            return render(request,'accounts/register.html',{'form':form})
            
    return render(request,'accounts/register.html',{'form':UserCreationForm})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # data{
            #     'username': 'Sachin',
            #     'password': '12345678'            
            # }
            # print(data['username'])
            # print(data['password'])
            user = authenticate(username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return redirect("/books/")
            else:
                messages.add_message(request,messages.ERROR,"Invalid username or password")
    return render(request, 'accounts/login.html',{'form':LoginForm})

def logout_user(request):
    logout(request)
    return redirect("/")
