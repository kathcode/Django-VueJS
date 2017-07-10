# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_cbv', '0007_auto_20161202_0407'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='name_animal',
            field=models.CharField(default=23, max_length=500),
            preserve_default=False,
        ),
    ]
