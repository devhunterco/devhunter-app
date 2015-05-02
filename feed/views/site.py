from django.shortcuts import render
from foro.models.user import User
from feed.models import Event
from django.conf import settings
from foro.models.category import Category
from foro.models.topic import Topic


def landing(request):
    topics = Topic.objects.for_public().filter(is_pinned=False)
    topics_pinned = Topic.objects.filter(category_id=settings.ST_UNCATEGORIZED_CATEGORY_PK,
                                         is_removed=False,
                                         is_pinned=True)
    topics = topics | topics_pinned
    topics = topics.order_by('-is_pinned', '-last_active').select_related('category')
    categories = Category.objects.for_parent()
    miembros_email = User.objects.filter(es_destacado=True)
    miembros_count = User.objects.filter(is_active=True).count()
    events = Event.objects.all()
    return render(request, 'site/landing.html',
                  {'miembros_email': miembros_email,
                   'miembros_count': miembros_count,
                   'events': events,
                   'categories': categories,
                   'topics': topics})


def about(request):
    return render(request, 'site/about.html')


def agenda(request):
    return render(request, 'site/agenda.html')


def miembros(request):
    miembros_activos = User.objects.order_by('date_joined').filter(is_active=True)
    return render(request, 'site/miembros.html',
                    {'miembros':miembros_activos,})
