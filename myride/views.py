from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myride/index.html')

def rate(request):
    return render(request,'myride/rate.html')
# later remove the below two functions and we'll just filter the results on
# on index page of myride based on start/end date and current date
def upcoming(request):
    return render(request, 'myride/upcoming.html')

def previous(request):
    return render(request, 'myride/previous.html')
