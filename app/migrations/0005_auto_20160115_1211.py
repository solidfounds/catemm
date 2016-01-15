# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20160115_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segundoregistro',
            name='credito',
            field=models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=7),
        ),
    ]
