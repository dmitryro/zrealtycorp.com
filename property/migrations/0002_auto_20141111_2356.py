# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='neighborhood',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'borough', to='property.Neighborhood', chained_field=b'borough'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='property',
            name='neighborhood',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'borough', to='property.Neighborhood', chained_field=b'borough'),
            preserve_default=True,
        ),
    ]
