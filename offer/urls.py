from django.conf.urls import url
from . import views

app_name = 'offer'

urlpatterns = [
    #/offer/<userid>/
    url(r'^(?P<userid>[0-9]+)/$', views.index, name = 'index'),
    #/offer/<userid>/offerdetails
    url(r'^(?P<userid>[0-9]+)/offerdetails/', views.offerdetails, name = 'offerdetails'),
]
