# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_auto_20141111_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='slug',
        ),
    ]
