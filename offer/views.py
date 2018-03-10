from django.shortcuts import render

def index(request):
    return render(request,'offer/offerindex.html')

def offerdetails(request):
    return render(request,'offer/offerdetails.html')
