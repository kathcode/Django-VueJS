# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books_cbv', '0013_auto_20170710_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 10, 16, 0, 20, 296438), max_length=200),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 10, 16, 0, 20, 298616), max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 10, 16, 0, 20, 294471), max_length=200),
        ),
        migrations.AlterField(
            model_name='historia',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 10, 16, 0, 20, 300692), max_length=200),
        ),
    ]
