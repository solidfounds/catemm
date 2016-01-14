# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrimerRegistro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=55)),
                ('apellidos', models.CharField(max_length=80)),
                ('direccion', models.TextField()),
                ('nsn', models.CharField(max_length=15)),
                ('telefono', models.SmallIntegerField()),
                ('empresa', models.CharField(max_length=254)),
                ('registro_patronal', models.CharField(max_length=15)),
                ('comision', models.DecimalField(max_digits=7, decimal_places=2)),
                ('ife', models.FileField(upload_to='media/ifes')),
                ('email', models.EmailField(max_length=254)),
                ('numero_de_cuenta', models.CharField(max_length=16)),
                ('banco', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Primer Registro',
            },
        ),
        migrations.CreateModel(
            name='SegundoRegistro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('caratula', models.CharField(max_length=50)),
                ('tarjeda_de_mejoravit', models.FileField(upload_to='media/targeta_infonavit')),
                ('cliente', models.ForeignKey(to='app.PrimerRegistro')),
            ],
            options={
                'verbose_name_plural': 'Segundo Registro',
            },
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('telefono', models.SmallIntegerField()),
                ('renta', models.DecimalField(max_digits=7, decimal_places=2)),
                ('luz', models.DecimalField(max_digits=7, decimal_places=2)),
                ('agua', models.DecimalField(max_digits=7, decimal_places=2)),
                ('varios', models.DecimalField(max_digits=7, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Sucursales',
            },
        ),
        migrations.CreateModel(
            name='TercerRegistro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('compra', models.TextField()),
                ('importe_total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('efectivo', models.DecimalField(max_digits=10, decimal_places=2)),
                ('comision', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('numero_credito', models.CharField(max_length=10)),
                ('cliente', models.ForeignKey(to='app.PrimerRegistro')),
            ],
            options={
                'verbose_name_plural': 'Tercer Registro',
            },
        ),
    ]
