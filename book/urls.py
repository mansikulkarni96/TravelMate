from django.conf.urls import url
from . import views

app_name = 'book'

urlpatterns = [
    #/book/
    url(r'^$', views.index, name = 'index'),
    #/book/search
    url(r'^search/', views.searchres, name = 'searchres'),
    #/book/bookdetails
    url(r'^bookdetails/', views.bookdetails, name = 'bookdetails'),
    #/book/confirm
    url(r'^confirm/', views.confirm, name = 'confirm'),
]
