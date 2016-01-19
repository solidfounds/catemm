# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160119_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segundoregistro',
            name='operador',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
