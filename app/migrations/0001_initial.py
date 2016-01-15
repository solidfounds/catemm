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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=55)),
                ('apellidos', models.CharField(max_length=80)),
                ('direccion', models.TextField()),
                ('nsn', models.CharField(max_length=15)),
                ('telefono', models.SmallIntegerField()),
                ('empresa', models.CharField(max_length=254)),
                ('registro_patronal', models.CharField(max_length=15)),
                ('comision', models.DecimalField(decimal_places=2, max_digits=7)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('caratula', models.CharField(max_length=50)),
                ('tarjeda_de_mejoravit', models.FileField(upload_to='media/targeta_infonavit')),
                ('targeta_entregada', models.BooleanField()),
                ('targeta_activa', models.BooleanField()),
                ('targeta_con_fondos', models.BooleanField()),
                ('credito', models.DecimalField(decimal_places=2, max_digits=7)),
                ('cliente', models.ForeignKey(to='app.PrimerRegistro')),
            ],
            options={
                'verbose_name_plural': 'Segundo Registro',
            },
        ),
        migrations.CreateModel(
            name='TercerRegistro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('compra', models.TextField()),
                ('importe_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('efectivo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('comision', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('numero_credito', models.CharField(max_length=10)),
                ('cliente', models.ForeignKey(to='app.PrimerRegistro')),
            ],
            options={
                'verbose_name_plural': 'Tercer Registro',
            },
        ),
    ]
