# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_calendarevent_lugar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='description',
            field=models.TextField(null=True, verbose_name='Descrip', blank=True),
            preserve_default=True,
        ),
    ]
