# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenancepage',
            name='avatar',
            field=models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Avatar', blank=True),
            preserve_default=True,
        ),
    ]
