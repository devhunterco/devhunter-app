from __future__ import unicode_literals

from django.conf.urls import patterns, url
from views import event_detail


urlpatterns = patterns('evento.views',
                       url(r'^(?P<id_event>\d+)/',
                           event_detail,
                           name='event-detail'),
                       )
