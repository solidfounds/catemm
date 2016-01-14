# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('telefono', models.SmallIntegerField()),
                ('renta', models.DecimalField(decimal_places=2, max_digits=7)),
                ('luz', models.DecimalField(decimal_places=2, max_digits=7)),
                ('agua', models.DecimalField(decimal_places=2, max_digits=7)),
                ('varios', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
            options={
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='sucursal',
            field=models.ForeignKey(to='users.Sucursal'),
        ),
    ]
