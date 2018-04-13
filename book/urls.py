from django.conf.urls import url
from . import views

app_name = 'book'

urlpatterns = [
    #/book/<userid>/
    url(r'^(?P<userid>[0-9]+)/$', views.index, name = 'index'),
    #/book/<userid>/search
    url(r'^(?P<userid>[0-9]+)/search/', views.searchres, name = 'searchres'),
    #/book/<userid>/bookdetails
    url(r'^(?P<userid>[0-9]+)/bookdetails/', views.bookdetails, name = 'bookdetails'),
]
