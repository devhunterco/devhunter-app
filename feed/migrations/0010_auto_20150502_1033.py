# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0009_auto_20150501_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='evento',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
