# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from agenda.models import CalendarEvent


def event_detail(request, id_event):
    event = get_object_or_404(CalendarEvent, pk=id_event)
    return render(request, 'evento/event_detail.html',
                  {'event': event})