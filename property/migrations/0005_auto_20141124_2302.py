# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20141124_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='is_featured'),
            preserve_default=True,
        ),
    ]
