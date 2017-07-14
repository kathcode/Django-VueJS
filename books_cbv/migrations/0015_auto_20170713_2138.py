# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books_cbv', '0014_auto_20170710_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 13, 21, 38, 53, 974231), max_length=200),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha_cita',
            field=models.DateField(default=datetime.date(2017, 7, 14)),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 13, 21, 38, 53, 976155), max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 13, 21, 38, 53, 971909), max_length=200),
        ),
        migrations.AlterField(
            model_name='historia',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 13, 21, 38, 53, 978092), max_length=200),
        ),
    ]
