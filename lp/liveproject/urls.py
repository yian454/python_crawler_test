from django.conf.urls import *
from django.contrib import admin

#from django.contrib.admin.sites import AdminSite, site

urlpatterns = patterns('',
	url(r'^admin/', admin.site.urls),
	url(r'^liveupdate/', include('liveproject.liveupdate.urls')),
)

#urlpatterns = patterns('',
#    url(r'^admin/(.*)', admin.site.index),
#	url(r'^admin/', admin.site.index),
#    url(r'^', include('liveproject.liveupdate.urls')),
#)
