# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20160129_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segundoregistro',
            name='tarjeta_activa',
        ),
        migrations.RemoveField(
            model_name='segundoregistro',
            name='tarjeta_entregada',
        ),
        migrations.RemoveField(
            model_name='segundoregistro',
            name='tarjeta_fondos',
        ),
        migrations.AlterField(
            model_name='primerregistro',
            name='telefono',
            field=models.PositiveIntegerField(verbose_name='teléfono'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='segundoregistro',
            name='numero_tarjeta',
            field=models.PositiveIntegerField(verbose_name='número de tarjeta'),
        ),
    ]
