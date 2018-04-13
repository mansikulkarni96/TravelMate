from django.shortcuts import render,get_object_or_404
from .models import User as GenUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login


def index(request):
    return render(request,'travel/index.html')

def login(request):
    return render(request,'travel/login.html')

def loginsubmit(request):
    mailid = request.POST.get('mail')
    username = mailid.split('@',1)[0]
    password = request.POST.get('password')
    user = authenticate(username = username, password = password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            loggeduser = get_object_or_404(GenUser,email = mailid)
            request.session['userid'] = loggeduser.id
            request.session['username'] = user.username
            return render(request,'travel/index.html')
    context = {'error':"Enter Valid Credentials"}
    return render(request,'travel/login.html',context)

def register(request):
    return render(request,'travel/register.html')

def registersubmit(request):
    genuser = GenUser()
    genuser.fname = request.POST.get('fname')
    genuser.lname = request.POST.get('lname')
    genuser.phone = request.POST.get('number')
    genuser.email = request.POST.get('mail')
    mailid = request.POST.get('mail')
    user = User()
    user.username = mailid.split('@',1)[0]
    password = request.POST.get('password')
    user.set_password(password)
    user.save()
    genuser.save()
    loggeduser = get_object_or_404(GenUser,email = mailid)
    request.session['userid'] = loggeduser.id
    request.session['username'] = user.username
    return render(request,'travel/index.html')


def logout_view(request):
    if request.session.has_key('username'):
        del request.session['username']
    if request.session.has_key('userid'):
        del request.session['userid']
    logout(request)
    return render(request,'travel/index.html')
