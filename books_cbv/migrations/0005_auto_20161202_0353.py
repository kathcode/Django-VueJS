# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_cbv', '0004_auto_20161201_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='fecha_creacion',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
