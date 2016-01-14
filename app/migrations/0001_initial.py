# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=70)),
                ('porcentaje_ganancia', models.CharField(max_length=1, choices=[('3', '3%'), ('4', '4%'), ('5', '5%'), ('6', '6%')])),
                ('clave', models.CharField(max_length=10)),
                ('num_de_cuenta', models.CharField(max_length=20)),
                ('banco', models.CharField(max_length=50)),
                ('telefono_casa', models.SmallIntegerField()),
                ('telefono_celular', models.SmallIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('ife', models.FileField(upload_to='media/empleados/ifes')),
                ('tipo_personal', models.CharField(max_length=1, choices=[('1', 'Asesor'), ('2', 'Asistente')])),
            ],
            options={
                'verbose_name_plural': 'Asesor',
            },
        ),
        migrations.CreateModel(
            name='PrimerRegistro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
                ('operador', models.OneToOneField(to='app.Personal')),
            ],
            options={
                'verbose_name_plural': 'Primer Registro',
            },
        ),
        migrations.CreateModel(
            name='SegundoRegistro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
        migrations.CreateModel(
            name='TercerRegistro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
        migrations.AddField(
            model_name='personal',
            name='sucursal',
            field=models.OneToOneField(to='app.Sucursales'),
        ),
    ]
