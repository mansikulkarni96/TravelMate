from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    # first landing page - /
    url(r'^$', include('travel.urls')),
    #admin url - /admin
    url(r'^admin/', admin.site.urls),
    #book url - /book
    url(r'^book/', include('book.urls')),
    #offer url - /offer
    url(r'^offer/', include('offer.urls')),
    #myride url - /myride
    url(r'^myride/', include('myride.urls')),
]
