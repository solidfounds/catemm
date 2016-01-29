# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160129_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segundoregistro',
            name='tarjeta_con_fondos',
        ),
        migrations.AddField(
            model_name='segundoregistro',
            name='tarjeta_fondos',
            field=models.BooleanField(verbose_name='tarjeta con fondos', default=True),
            preserve_default=False,
        ),
    ]
