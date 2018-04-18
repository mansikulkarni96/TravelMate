from django.conf.urls import url
from . import views

app_name = 'offer'

urlpatterns = [
    #/offer/<userid>/
    url(r'^(?P<userid>[0-9]+)/$', views.index, name = 'index'),
    #/offer/<userid>/offerdetails
    url(r'^(?P<userid>[0-9]+)/offerdetails/', views.offerdetails, name = 'offerdetails'),
    #/offer/<userid>/delete
    url(r'^(?P<userid>[0-9]+)/delete/', views.deleteride, name = 'deleteride'),
    #/offer/<userid>/offerings
    url(r'^(?P<userid>[0-9]+)/offerings/', views.allofferedrides, name = 'allofferedrides'),
]
