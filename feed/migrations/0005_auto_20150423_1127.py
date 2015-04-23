# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('serial', models.CharField(max_length=60, serialize=False, primary_key=True)),
                ('brand', models.CharField(max_length=30)),
                ('device', models.CharField(max_length=2, choices=[('PC', 'PC'), ('TB', 'Tablet')])),
            ],
            options={
                'verbose_name': 'Dispositivos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('national_id', models.CharField(max_length=60, serialize=False, primary_key=True)),
                ('fist_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Asistente',
                'verbose_name_plural': 'Asistentes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(to='feed.Person'),
            preserve_default=True,
        ),
    ]
