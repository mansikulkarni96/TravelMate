from django.shortcuts import render



def index(request):
    return render(request,'travel/index.html')

def login(request):
    return render(request,'travel/login.html')

def register(request):
    return render(request,'travel/register.html')
