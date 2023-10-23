from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def demo(request):
    return render(request,"home.html")


def signup(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request,"username already taken")
            return redirect('signup')

        elif User.objects.filter(email=email).exists():
            messages.info(request,"email already in use")
            return redirect('signup')

        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save();print("user created")
            return redirect('login')
    return render(request,"signup.html")



def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('signup')

        else:
            messages.info(request,"invalid")
            return HttpResponse("invalid")


    return render(request,"login.html")


def logout(request):
    auth.logout(request)
    return redirect('signup')