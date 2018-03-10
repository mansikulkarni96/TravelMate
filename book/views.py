from django.shortcuts import render


def index(request):
    return render(request,'book/bookindex.html')

def searchres(request):
    return render(request,'book/search.html')

def bookdetails(request):
    return render(request,'book/bookdetails.html')

def confirm(request):
    return render(request,'book/confirm.html')
