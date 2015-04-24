# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_auto_20150423_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='color',
            field=models.CharField(default='None', max_length=30),
            preserve_default=True,
        ),
    ]
