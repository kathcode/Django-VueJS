# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books_cbv', '0012_auto_20170710_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='historia',
            name='name',
            field=models.CharField(default=b'name', max_length=500),
        ),
        migrations.AlterField(
            model_name='animal',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 10, 15, 57, 47, 103185), max_length=200),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 10, 15, 57, 47, 105403), max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 10, 15, 57, 47, 101269), max_length=200),
        ),
        migrations.AlterField(
            model_name='historia',
            name='fecha_creacion',
            field=models.CharField(default=datetime.datetime(2017, 7, 10, 15, 57, 47, 107305), max_length=200),
        ),
    ]
