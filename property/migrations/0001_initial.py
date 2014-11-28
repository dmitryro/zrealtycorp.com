# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borough',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borough', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('borough', models.ForeignKey(to='property.Borough')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('neighborhood', models.CharField(max_length=30)),
                ('borough', models.ForeignKey(to='property.Borough')),
            ],
            options={
                'verbose_name': 'neighborhood',
                'verbose_name_plural': 'neighborhoods',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('property_id', models.IntegerField(default=1, null=True, blank=True)),
                ('title', models.CharField(max_length=500)),
                ('fulltitle', models.CharField(max_length=1600, null=True, blank=True)),
                ('price', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=30)),
                ('bathrooms', models.IntegerField(null=True, blank=True)),
                ('description', models.TextField(max_length=2400)),
                ('published', models.DateTimeField(verbose_name=b'Date Published')),
                ('expires', models.DateTimeField(verbose_name=b'Date expires')),
                ('pets_allowed', models.BooleanField(default=False, verbose_name='allow sorting')),
                ('is_featured', models.BooleanField(default=False, verbose_name='allow sorting')),
                ('slug', models.SlugField(help_text=b'A "slug" is a unique URL-friendly title for an object.', unique=True, verbose_name=b'title slug')),
                ('picture1', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Property View 1', blank=True)),
                ('picture2', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Property View 2', blank=True)),
                ('picture3', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Property View 3', blank=True)),
                ('picture4', models.ImageField(upload_to=b'images/', null=True, verbose_name=b'Property View 4', blank=True)),
                ('borough', models.ForeignKey(to='property.Borough')),
                ('category', models.ForeignKey(to='property.Category')),
                ('neighborhood', smart_selects.db_fields.ChainedForeignKey(to='property.Neighborhood')),
            ],
            options={
                'ordering': ('property_id',),
                'verbose_name': 'property',
                'verbose_name_plural': 'properties',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rooms', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'bed rooms',
                'verbose_name_plural': 'bed rooms',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'status',
                'verbose_name_plural': 'statuses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'property type',
                'verbose_name_plural': 'property types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='property',
            name='rooms',
            field=models.ForeignKey(blank=True, to='property.Room', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.ForeignKey(to='property.Status'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='property',
            name='type',
            field=models.ForeignKey(to='property.Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='location',
            name='neighborhood',
            field=smart_selects.db_fields.ChainedForeignKey(to='property.Neighborhood'),
            preserve_default=True,
        ),
    ]
