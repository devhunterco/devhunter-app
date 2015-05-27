from django.conf import settings
from django.shortcuts import render
from foro.models.user import User
from foro.models.category import Category
from foro.models.topic import Topic
from agenda.models import CalendarEvent
from django.db.models import Q
import datetime

def home(request):
    topics = Topic.objects.for_public().filter(is_pinned=False)
    topics_pinned = Topic.objects.filter(category_id=settings.ST_UNCATEGORIZED_CATEGORY_PK,
                                         is_removed=False,
                                         is_pinned=True)
    topics = topics | topics_pinned
    topics = topics.order_by('-is_pinned', '-last_active').select_related('category')
    categories = Category.objects.for_parent()
    miembros_email = User.objects.filter(es_destacado=True)
    miembros_count = User.objects.all().count()
    today = datetime.datetime.today()
    past_actividades = CalendarEvent.objects.filter(Q(start__lte=today))
    past_actividades_count = CalendarEvent.objects.filter(Q(start__lte=today)).count()
    prox_actividades = CalendarEvent.objects.filter(Q(start__gte=today))
    prox_actividades_count = CalendarEvent.objects.filter(Q(start__gte=today)).count()
    return render(request, 'devhunt/home.html',
                  {'miembros_email': miembros_email,
                   'miembros_count': miembros_count,
                   'categories': categories,
                   'topics': topics,
                   'prox_actividades': prox_actividades,
                   'prox_actividades_count': prox_actividades_count,
                   'past_actividades': past_actividades,
                   'past_actividades_count': past_actividades_count,
                   })


def miembros(request):
    miembros_activos = User.objects.order_by('date_joined').filter(is_active=True)
    return render(request, 'devhunt/miembros.html',
                           {'miembros_activos': miembros_activos})