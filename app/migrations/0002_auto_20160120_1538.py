# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='segundoregistro',
            name='operador',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='primerregistro',
            name='operador',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='detalleventa_',
            name='producto',
            field=models.ForeignKey(to='app.Productos'),
        ),
        migrations.AddField(
            model_name='detalleventa_',
            name='venta',
            field=models.ForeignKey(to='app.Venta'),
        ),
    ]
