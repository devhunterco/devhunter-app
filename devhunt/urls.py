# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',

                       url(r'^$', 'devhunt.views.home',
                                  name='home'),
                       url(r'^miembros/', 'devhunt.views.miembros',
                                          name='miembros'),
                       url(r'^sobre/', 'devhunt.views.sobre',
                                       name='about'),

                       url(r'^devhunt/', include(admin.site.urls)),

			           url(r'^agenda/', include('agenda.urls',
					    							   namespace="agenda",
					    							   app_name="agenda")),

              url(r'^discusiones/', include('foro.urls',
                                   namespace="foro",
                                   app_name="foro")),
              url(r'^eventos/', include('evento.urls',
                                  namespace="evento")),
                      )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
