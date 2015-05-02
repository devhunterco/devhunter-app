# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0008_person_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='brand',
            field=models.CharField(max_length=30, verbose_name='Marca'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='device',
            field=models.CharField(max_length=2, verbose_name='Tipo de Dispositivo', choices=[('PC', 'PC'), ('TB', 'Tablet')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(verbose_name='Propietario', to='feed.Person'),
            preserve_default=True,
        ),
    ]
