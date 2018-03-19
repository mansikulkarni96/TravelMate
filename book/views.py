from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Reservation
from .models import Enlist

def index(request):
    return render(request,'book/bookindex.html')

def searchres(request):
    all_reservations = Reservation.objects.all()
    context = {
        'all_reservations': all_reservations,
    }
    return render(request,'book/search.html', context)


def bookdetails(request):
    return render(request,'book/bookdetails.html')

def confirm(request):
    return render(request,'book/confirm.html')
