from django.shortcuts import render
from foro.models.user import User


def landing(request):
    miembros_email = User.objects.filter(es_destacado=True)
    miembros_count = User.objects.filter(is_active=True).count()
    return render(request, 'site/landing.html',
                  {'miembros_email': miembros_email,
                   'miembros_count': miembros_count,
                   })


def about(request):
    return render(request, 'site/about.html')


def agenda(request):
    return render(request, 'site/agenda.html')


def miembros(request):
    miembros_activos = User.objects.order_by('date_joined').filter(is_active=True)
    return render(request, 'site/miembros.html',
                           {'miembros': miembros_activos})
