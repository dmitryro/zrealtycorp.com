# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMetaProp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('address1', models.CharField(max_length=150)),
                ('address2', models.CharField(max_length=150, null=True, blank=True)),
                ('city', models.CharField(max_length=150)),
                ('zip', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('fax', models.CharField(max_length=20)),
                ('hours', models.CharField(max_length=200)),
                ('days', models.CharField(max_length=200)),
                ('note', models.CharField(max_length=1500, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'contact meta property',
                'verbose_name_plural': 'contact meta properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MetaProp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140)),
                ('keywords', models.CharField(max_length=1600)),
                ('description', models.TextField(max_length=1500)),
                ('author', models.CharField(max_length=140)),
                ('analytics', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'meta property',
                'verbose_name_plural': 'meta properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfileMetaProp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150, null=True, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('from_email', models.EmailField(max_length=75)),
                ('smtp_server', models.CharField(max_length=150)),
                ('smtp_port', models.CharField(max_length=10)),
                ('user_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('moto', models.CharField(max_length=250, null=True, blank=True)),
                ('message', models.CharField(max_length=2500, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'profile meta property',
                'verbose_name_plural': 'profile meta properties',
            },
            bases=(models.Model,),
        ),
    ]
