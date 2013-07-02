
from django.conf.urls import patterns, url

import reader.views

urlpatterns = patterns('',
    url(r'^$', reader.views.index, name='index'),
    url(r'^token/(?P<user_name>\w+)$', reader.views.getToken, name='getToken'),
    url(r'^record/(?P<user_name>\w+)/(?P<verifier>\d+)$', reader.views.recordToken, name='recordToken'),
    url(r'^tl/(?P<user_name>\w+)$', reader.views.timeline, name='timeline'),
)
