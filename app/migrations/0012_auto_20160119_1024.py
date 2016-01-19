# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0011_auto_20160119_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primerregistro',
            name='operador',
        ),
        migrations.AddField(
            model_name='primerregistro',
            name='operador',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
