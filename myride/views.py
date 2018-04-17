from django.shortcuts import render,get_object_or_404
from book.models import Reservation
from offer.models import Enlist
from travel.models import User
from datetime import datetime
from datetime import date

# Create your views here.

def index(request):
    print(request.session['userid'])
    all_reservations = Reservation.objects.all().filter(uid = request.session['userid'],start_date__lt = date.today())
    print(all_reservations)
    context  = {
        'all_reservations': all_reservations
    }
    return render(request, 'myride/index.html', context)

def rate(request):
    return render(request,'myride/rate.html')
# later remove the below two functions and we'll just filter the results on
# on index page of myride based on start/end date and current date
def upcoming(request):
    all_reservations = Reservation.objects.all().filter(uid = request.session['userid'],start_date__gte = date.today())
    print(all_reservations)
    context  = {
        'all_reservations': all_reservations
    }
    return render(request, 'myride/upcoming.html', context)

def previous(request):
    return render(request, 'myride/previous.html')
