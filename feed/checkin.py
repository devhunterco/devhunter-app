# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    national_id = models.CharField(("Cédula"), max_length=60, primary_key=True)
    fist_name = models.CharField(("Nombre"), max_length=30)
    last_name = models.CharField(("Apellido"), max_length=30)
    asistencia = models.BooleanField(("Asistencia"), default=False)
    email = models.EmailField(("Correo"), default="None")

    def __unicode__(self):
        return unicode(self.national_id)

    class Meta:
        verbose_name = "Asistente"
        verbose_name_plural = "Asistentes"


class Device(models.Model):
    PC = 'PC'
    TABLET = 'TB'
    TIPE_DEVICE = (
        (PC, 'PC'),
        (TABLET, 'Tablet')
    )
    serial = models.CharField(max_length=60, primary_key=True)
    brand = models.CharField(("Marca"), max_length=30)
    device = models.CharField(("Tipo de Dispositivo"), max_length=2, choices=TIPE_DEVICE)
    owner = models.ForeignKey(Person, verbose_name='Propietario')
    color = models.CharField(max_length=30, default="None")

    def __unicode__(self):
        return unicode(self.serial)

    class Meta:
        verbose_name = "Dispositivo"
        verbose_name_plural = "Dispositivos"
