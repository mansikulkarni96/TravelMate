from django.shortcuts import render,get_object_or_404
from .models import Enlist
from travel.models import User
from datetime import datetime


def index(request,userid):
    context = {'userid':userid}
    if request.session.has_key('userid') and request.session['userid'] == int(userid):
        return render(request,'offer/offerindex.html', context)
    else:
        return render(request,'travel/index.html')


def offerdetails(request,userid):
    #print(request.POST)
    if request.session.has_key('userid') and request.session['userid'] == int(userid):
        user = get_object_or_404(User,pk = userid)
        ent = Enlist()
        ent.uid = user
        ent.car_model =request.POST.get('car')
        ent.car_no = request.POST.get('car_no')
        ent.seat = request.POST.get('seats')
        ent.from_loc = request.POST.get('fromlocation')
        ent.to_loc = request.POST.get('tolocation')
        ent.fare = request.POST.get('fare')
        ent.start_time =request.POST.get('start_time')
        #print request.POST.get('return_time')
        ent.return_time =request.POST.get('start_time') # TODO needs to be changed later
        startdate = request.POST.get('start_date')
        parsed_date = datetime.strptime(str(startdate), "%m/%d/%Y")
        ent.start_date = parsed_date
        ent.save()
        all_enlists = Enlist.objects.filter(uid = user)
        #print all_enlists
        context = {'all_enlists':all_enlists}
        return render(request,'offer/offerdetails.html',context)
    else:
        return render(request,'travel/index.html')
