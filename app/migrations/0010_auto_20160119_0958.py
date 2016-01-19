# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160118_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segundoregistro',
            old_name='targeta_activa',
            new_name='tarjeta_activa',
        ),
        migrations.RenameField(
            model_name='segundoregistro',
            old_name='targeta_con_fondos',
            new_name='tarjeta_con_fondos',
        ),
        migrations.RenameField(
            model_name='segundoregistro',
            old_name='targeta_entregada',
            new_name='tarjeta_entregada',
        ),
    ]
