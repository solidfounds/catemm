# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_segundoregistro_operador'),
    ]

    operations = [
        migrations.RenameField(
            model_name='segundoregistro',
            old_name='tarjeda_de_mejoravit',
            new_name='tarjeta_de_mejoravit',
        ),
        migrations.AddField(
            model_name='segundoregistro',
            name='numero_tarjeta',
            field=models.SmallIntegerField(default=121221),
            preserve_default=False,
        ),
    ]
