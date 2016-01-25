# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160121_1045'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ComisionEmpleados',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=7)),
                ('liquidado', models.BooleanField()),
                ('cliente', models.ForeignKey(to='app.SegundoRegistro')),
                ('operador', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Comisión Empleados',
            },
        ),
    ]
