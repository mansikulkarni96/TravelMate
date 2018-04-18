from django.shortcuts import render,get_object_or_404
from .models import Reservation
from offer.models import Enlist
from travel.models import User
from myride.views import upcoming
from datetime import datetime

# get form data here and

def index(request,userid):
    context = {'userid':userid}
    if request.session.has_key('userid') and request.session['userid'] == int(userid):
        return render(request,'book/bookindex.html',context)
    else:
        return render(request,'travel/index.html')




def searchres(request,userid):
    # print(request.POST)
    if request.session.has_key('userid') and request.session['userid'] == int(userid):
        fromlocation = request.POST.get('fromlocation')
        tolocation = request.POST.get('tolocation')
        departure = request.POST.get('departure')
        context = {'error': 'Enter the details'}
        if departure and fromlocation and tolocation :
            parsed_date = datetime.strptime(str(departure), "%m/%d/%Y")
            all_enlists = Enlist.objects.filter(from_loc=fromlocation,to_loc=tolocation,start_date = parsed_date,seat__gte=1).order_by('start_time')
            context = {
                'all_enlists': all_enlists,
                'fromlocation': fromlocation,
                'tolocation': tolocation,
                'departure': departure
            }
            #print(departure)
        return render(request,'book/search.html',context)
    else:
        return render(request,'travel/index.html')



def bookdetails(request,userid):
    if request.session.has_key('userid') and request.session['userid'] == int(userid):
        enlistid = request.POST.get('eid')
        user = get_object_or_404(User,pk = userid)
        enlist = get_object_or_404(Enlist,pk = enlistid)
        if enlist.uid.pk != user.pk:
            reservation = Reservation()
            reservation.uid = user
            reservation.eid = enlist
            reservation.from_loc = enlist.from_loc
            reservation.to_loc = enlist.to_loc
            reservation.start_date = enlist.start_date
            reservation.save()
            seat = enlist.seat
            seat = seat - 1
            enlist.seat = seat
            enlist.save()
            return upcoming(request)
        else:
            context = {
                'error': "Please select an offered ride which is not provided by you.",
                'fromlocation': enlist.from_loc,
                'tolocation': enlist.to_loc
            }
            return render(request, 'book/search.html', context)
    else:
        return render(request,'travel/index.html')
