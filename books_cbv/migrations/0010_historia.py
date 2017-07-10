# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books_cbv', '0009_auto_20161202_0440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_historia', models.IntegerField()),
                ('id_animal', models.IntegerField()),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha_creacion', models.CharField(default=datetime.datetime(2017, 7, 9, 6, 31, 5, 154398), max_length=200)),
            ],
        ),
    ]
