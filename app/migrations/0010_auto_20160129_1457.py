# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160129_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segundoregistro',
            name='tarjeta_de_mejoravit',
            field=models.FileField(upload_to='media/targeta_infonavit', blank=True, null=True),
        ),
    ]
