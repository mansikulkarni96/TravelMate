from django.conf.urls import url
from . import views

app_name = 'travel'

urlpatterns = [
    #/
    url(r'^$', views.index, name = 'index'),
    #/login
    url(r'^login/', views.login, name = 'login'),
    #/login
    url(r'^loginsubmit/', views.loginsubmit, name = 'loginsubmit'),
    #/register
    url(r'^register/', views.register, name = 'register'),
    #/registersubmit
    url(r'^registersubmit/', views.registersubmit, name = 'registersubmit'),
    #/signout
    url(r'^signout/', views.logout_view, name = 'signout'),
]
