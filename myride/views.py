from django.shortcuts import render,get_object_or_404
from book.models import Reservation
from offer.models import Enlist
from travel.models import User
from datetime import datetime
from datetime import date

# Create your views here.

def index(request):
    all_reservations = Reservation.objects.all().filter(uid = request.session['userid'],start_date__lt = date.today())
    context  = {
        'all_reservations': all_reservations
    }
    return render(request, 'myride/index.html', context)

def rate(request):
    return render(request,'myride/rate.html')

def upcoming(request):
    all_reservations = Reservation.objects.all().filter(uid = request.session['userid'],start_date__gte = date.today())
    context  = {
        'all_reservations': all_reservations
    }
    return render(request, 'myride/upcoming.html', context)

def previous(request):
    return render(request, 'myride/previous.html')
