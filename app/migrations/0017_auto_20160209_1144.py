# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20160209_1139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primerregistro',
            name='direccion',
        ),
        migrations.RemoveField(
            model_name='primerregistro',
            name='email',
        ),
        migrations.RemoveField(
            model_name='primerregistro',
            name='nsn',
        ),
        migrations.AddField(
            model_name='primerregistro',
            name='calle',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='primerregistro',
            name='colonia_o_fraccionamiento',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='primerregistro',
            name='cp',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='primerregistro',
            name='endidad',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='primerregistro',
            name='municipio_o_delegacion',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='primerregistro',
            name='nss',
            field=models.CharField(max_length=11, null=True, verbose_name=b'nss'),
        ),
        migrations.AddField(
            model_name='primerregistro',
            name='numero',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
