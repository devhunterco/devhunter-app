from django.conf import settings
from django.shortcuts import render
from foro.models.user import User
from django.shortcuts import get_object_or_404
from foro.models.category import Category
from foro.models.topic import Topic
from foro.models.comment import Comment
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
    miembros_count = User.objects.filter(is_active=True).count()
    today = datetime.datetime.today()
    past_actividades = CalendarEvent.objects.filter(Q(start__lte=today))[:3]
    past_actividades_count = CalendarEvent.objects.filter(Q(start__lte=today)).count()
    prox_actividades = CalendarEvent.objects.filter(Q(start__gte=today))
    prox_actividades_count = CalendarEvent.objects.filter(Q(start__gte=today)).count()
    lasted_comments = Comment.objects.order_by('-date')[:5]
    return render(request, 'devhunt/home.html',
                  {'miembros_email': miembros_email,
                   'miembros_count': miembros_count,
                   'categories': categories,
                   'topics': topics,
                   'prox_actividades': prox_actividades,
                   'prox_actividades_count': prox_actividades_count,
                   'past_actividades': past_actividades,
                   'past_actividades_count': past_actividades_count,
                   'lasted_comments': lasted_comments
                   })


def members(request):
    miembros_activos = User.objects.order_by('date_joined').filter(is_active=True)
    return render(request, 'devhunt/miembros.html',
                           {'miembros_activos': miembros_activos})


def member_profile(request, username):
    p_user = get_object_or_404(User, username=username)
    return render(request, 'devhunt/user/profile.html', {'p_user': p_user})


def sobre(request):
    return render(request, 'devhunt/about.html')


def slack(request):
    return render(request, 'devhunt/slack.html')
