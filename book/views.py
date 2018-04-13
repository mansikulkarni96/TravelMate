from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Reservation
from .models import Enlist

# get form data here and

def index(request):
    return render(request,'travel/index.html')




def searchres(request):
    # print(request.POST)
    fromlocation = request.POST.get('fromlocation')
    tolocation = request.POST.get('tolocation')
    departure = request.POST.get('departure')
    all_enlists = Enlist.objects.filter(from_loc=fromlocation,to_loc=tolocation)
    context = {
        'all_enlists': all_enlists,
        'fromlocation': fromlocation,
        'tolocation': tolocation,
        'departure': departure
    }
    #print(departure)
    return render(request,'book/search.html',context)

# def get(self, request):
#     form = IndexForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'book/bookindex.html', context)

def bookdetails(request):
    return render(request,'book/bookdetails.html')

def confirm(request):
    return render(request,'book/confirm.html')
