# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books_cbv', '0011_auto_20170709_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 10, 15, 53, 45, 164268), max_length=200),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 10, 15, 53, 45, 166456), max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 10, 15, 53, 45, 162318), max_length=200),
        ),
        migrations.AlterField(
            model_name='historia',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 10, 15, 53, 45, 168561), max_length=200),
        ),
    ]
