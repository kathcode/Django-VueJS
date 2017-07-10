# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books_cbv', '0010_historia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 9, 6, 31, 32, 243229), max_length=200),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 9, 6, 31, 32, 245124), max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 9, 6, 31, 32, 240039), max_length=200),
        ),
        migrations.AlterField(
            model_name='historia',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 9, 6, 31, 32, 246860), max_length=200),
        ),
    ]
