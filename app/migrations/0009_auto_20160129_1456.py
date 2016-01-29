# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_order_operador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segundoregistro',
            name='tarjeta_de_mejoravit',
            field=models.FileField(blank=True, upload_to='media/targeta_infonavit'),
        ),
    ]
