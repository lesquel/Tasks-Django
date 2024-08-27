from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
# Create your views here.
def singUp(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        try:
            userName = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                user = User.objects.create_user(username=userName, password=password1)
                user.save()
                login(request, user)
                
                return redirect('index')
        except IntegrityError:
            return render(request, "singup.html", {
                "form":  UserCreationForm()
            })
        return render(request, "signup.html")

    return render(request,"singup.html", {
        "form":  UserCreationForm()
    })
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(password)
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        return render(request, 'login.html', {
            "form":  AuthenticationForm()
        })
    return render(request,'login.html', {
        "form":  AuthenticationForm()
    })
def logoutPage(request):
    logout(request)
    return redirect('loginPage')