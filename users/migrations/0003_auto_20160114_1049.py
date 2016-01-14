# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160114_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sucursal',
            field=models.ForeignKey(to='users.Sucursal', blank=True, null=True),
        ),
    ]
