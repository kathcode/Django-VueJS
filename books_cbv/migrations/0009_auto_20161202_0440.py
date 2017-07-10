# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_cbv', '0008_cita_name_animal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cita',
            old_name='name_animal',
            new_name='name',
        ),
    ]
