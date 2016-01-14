# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160114_1045'),
        ('app', '0002_primerregistro_operador'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sucursales',
        ),
    ]
