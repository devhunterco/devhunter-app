# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from agenda.models import CalendarEvent
from foro.models.user import User


def event_detail(request, id_event):
    event = get_object_or_404(CalendarEvent, pk=id_event)
    miembros_email = User.objects.filter(es_destacado=True)
    miembros_count = User.objects.filter(is_active=True).count()
    return render(request, 'evento/event_detail.html',
                  {'event': event,'miembros_email': miembros_email,
                   'miembros_count': miembros_count})
