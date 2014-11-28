# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_remove_property_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='is_feagured'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='pets_allowed',
            field=models.BooleanField(default=False, verbose_name='pets_allowed'),
            preserve_default=True,
        ),
    ]
