# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^$', 'feed.views.site.landing',
                           name='site-landing'),
                       url(r'^acerca/', 'feed.views.site.about',
                           name='site-about'),
                       url(r'^projects/',
                           'feed.views.project.projects_active',
                           name='projects-active'),
                       url(r'^project/publish',
                           'feed.views.project.project_publish',
                           name='project-publish'),
                       url(r'^project/detail/(?P<pk>\d+)/$',
                           'feed.views.project.project_detail',
                           name='project-detail'),
                       url(r'^project/update(?P<pk>\d+)/$',
                           'feed.views.project.project_update',
                           name='project-update'),
                       url(r'^event/(?P<id_event>\d+)$',
                           'feed.views.event.event_detail',
                           name='event-detail'),
                       url(r'^event/publish',
                           'feed.views.event.event_publish',
                           name='event-publish'),
                       url(r'^miembros/',
                           'feed.views.site.miembros',
                           name='miembros'),
                       url(r'^agenda/',
                           'feed.views.site.agenda',
                           name='agenda'),
                       )
