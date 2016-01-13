# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compras',
            name='articulos',
        ),
        migrations.AlterField(
            model_name='tercerregistro',
            name='compra',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Articulos',
        ),
        migrations.DeleteModel(
            name='Compras',
        ),
    ]
