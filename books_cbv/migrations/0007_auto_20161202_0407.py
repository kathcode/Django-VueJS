# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_cbv', '0006_auto_20161202_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='color',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='animal',
            name='fecha_creacion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='animal',
            name='fecha_nacim',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha_creacion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_creacion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=200),
        ),
    ]
