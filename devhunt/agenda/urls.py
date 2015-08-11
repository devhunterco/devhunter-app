# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from views import CalendarJsonListView, CalendarView

urlpatterns = patterns('agenda.views',
                       url(
                           r'^json/$',
                           CalendarJsonListView.as_view(),
                           name='calendar_json'
                       ),
                       url(
                           r'^$',
                           CalendarView.as_view(),
                           name='calendar'
                       ),
                       )
