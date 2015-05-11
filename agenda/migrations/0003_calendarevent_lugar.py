# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20150502_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendarevent',
            name='lugar',
            field=models.CharField(max_length=255, null=True, verbose_name='Lugar'),
            preserve_default=True,
        ),
    ]
