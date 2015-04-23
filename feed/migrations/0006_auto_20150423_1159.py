# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20150423_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'verbose_name': 'Dispositivo', 'verbose_name_plural': 'Dispositivos'},
        ),
        migrations.AddField(
            model_name='person',
            name='asistencia',
            field=models.BooleanField(default=False, verbose_name='Asistencia'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='fist_name',
            field=models.CharField(max_length=30, verbose_name='Nombre'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Apellido'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='national_id',
            field=models.CharField(max_length=60, serialize=False, verbose_name='C\xe9dula', primary_key=True),
            preserve_default=True,
        ),
    ]
