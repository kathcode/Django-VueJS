# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_cbv', '0003_auto_20161201_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='color',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AlterField(
            model_name='animal',
            name='fecha_nacim',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
