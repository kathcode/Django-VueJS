# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_cbv', '0002_auto_20161201_0313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('fecha_nacim', models.CharField(max_length=200)),
                ('id_cliente', models.IntegerField()),
                ('fecha_creacion', models.CharField(default=False, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('id_animal', models.IntegerField()),
                ('fecha_cita', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha_creacion', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='cliente',
            name='fecha_creacion',
            field=models.CharField(default=False, max_length=200),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
