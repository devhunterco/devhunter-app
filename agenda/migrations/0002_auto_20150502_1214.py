# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendarevent',
            name='description',
            field=models.TextField(max_length=255, null=True, verbose_name='Descrip', blank=True),
            preserve_default=True,
        ),
    ]
