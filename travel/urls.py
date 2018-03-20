from django.conf.urls import url
from . import views

app_name = 'travel'

urlpatterns = [
    #/
    url(r'^$', views.index, name = 'index'),
    #/login
    url(r'^login/', views.login, name = 'login'),
    #/register
    url(r'^register/', views.register, name = 'register'),
]
