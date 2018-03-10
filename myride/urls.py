from django.conf.urls import url
from . import views

app_name = 'myride'

urlpatterns = [
    #/myride/
    url(r'^$', views.index, name = 'index'),
    url(r'^rate/', views.rate, name = 'rate'),
    # later remove the below two functions and we'll just filter the results on
    # on index page of myride based on start/end date and current date
    url(r'^upcoming/', views.upcoming, name = 'upcoming'),
    url(r'^previous/', views.previous, name = 'previous'),
]
