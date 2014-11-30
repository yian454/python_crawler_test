from django.conf.urls import *

from liveproject.liveupdate.models import Update


urlpatterns = patterns('',
#	url(r'^updates/', 'django.views.generic.list.ListView', {'queryset': Update.objects.all()}),
#	url(r'^updates-after/(?P<id>\d+)/$', 'liveproject.liveupdate.views.updates_after'),
	url(r'^updates-after/(?P<id>\d+)/$', 'django.views.generic.list.ListView', {'self.queryset': Update.objects.all()}),
)
