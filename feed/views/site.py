from django.shortcuts import render
from foro.models.user import User
from feed.models import Event


def landing(request):
    miembros_email = User.objects.filter(es_destacado=True)
    miembros_count = User.objects.all().count()
    events = Event.objects.all()
    return render(request, 'site/landing.html',
                  {'miembros_email': miembros_email,
                   'miembros_count': miembros_count,
                   'events': events})


def about(request):
    return render(request, 'site/about.html')
