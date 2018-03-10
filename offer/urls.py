from django.conf.urls import url
from . import views

app_name = 'offer'

urlpatterns = [
    #/offer/
    url(r'^$', views.index, name = 'index'),
    #/offer/offerdetails
    url(r'^offerdetails/', views.offerdetails, name = 'offerdetails'),
]
