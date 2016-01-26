# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160126_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.AddField(
            model_name='order',
            name='orden_de_compra',
            field=models.CharField(default=1, max_length=1, choices=[('1', 'Orden de Compra 1'), ('2', 'Orden de Compra 2'), ('3', 'Orden de Compra 3')]),
            preserve_default=False,
        ),
    ]
