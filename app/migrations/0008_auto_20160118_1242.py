# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20160118_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='precio',
            new_name='price',
        ),
    ]
