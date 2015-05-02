# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('url', models.URLField(null=True, verbose_name='URL', blank=True)),
                ('css_class', models.CharField(max_length=20, verbose_name='CSS Class', choices=[(b'', 'Normal'), (b'event-warning', 'Warning'), (b'event-info', 'Info'), (b'event-success', 'Success'), (b'event-inverse', 'Inverse'), (b'event-special', 'Special'), (b'event-important', 'Important')])),
                ('start', models.DateTimeField(verbose_name='Start Date')),
                ('end', models.DateTimeField(null=True, verbose_name='End Date', blank=True)),
                ('description', models.TextField(max_length=255, null=True, verbose_name='Descrip')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
