# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('precio', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'verbose_name_plural': 'Articulos',
            },
        ),
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=70)),
                ('porcentaje_ganancia', models.CharField(choices=[('3', '3%'), ('4', '4%'), ('5', '5%'), ('6', '6%')], max_length=1)),
                ('clave', models.CharField(max_length=10)),
                ('num_de_cuenta', models.CharField(max_length=20)),
                ('banco', models.CharField(max_length=50)),
                ('telefono_casa', models.SmallIntegerField()),
                ('telefono_celular', models.SmallIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('ife', models.FileField(upload_to='media/empleados/ifes')),
            ],
            options={
                'verbose_name_plural': 'Asesor',
            },
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('tipo_compra', models.CharField(choices=[('1', 'Compra 1'), ('2', 'Compra 2')], max_length=1)),
                ('cantidad', models.SmallIntegerField()),
                ('total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('articulos', models.ForeignKey(to='app.Articulos')),
            ],
            options={
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='PrimerRegistro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=55)),
                ('apellidos', models.CharField(max_length=80)),
                ('direccion', models.TextField()),
                ('nsn', models.CharField(max_length=15)),
                ('telefono_casa', models.SmallIntegerField()),
                ('telefono_celular', models.SmallIntegerField()),
                ('empresa', models.CharField(max_length=254)),
                ('registro_patronal', models.CharField(max_length=15)),
                ('facturacion', models.CharField(max_length=254)),
                ('comision', models.DecimalField(max_digits=7, decimal_places=2)),
                ('acta_de_nacimiento', models.BooleanField()),
                ('ife', models.FileField(upload_to='media/ifes')),
                ('email', models.EmailField(max_length=254)),
                ('operador_que_lo_registro', models.OneToOneField(to='app.Asesor')),
            ],
            options={
                'verbose_name_plural': 'Primer Registro',
            },
        ),
        migrations.CreateModel(
            name='SegundoRegistro',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('caratula', models.CharField(max_length=50)),
                ('tarjeda_de_mejoravit', models.FileField(upload_to='media/targeta_infonavit')),
                ('numero_cuenta', models.CharField(max_length=50)),
                ('banco', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(to='app.PrimerRegistro')),
            ],
            options={
                'verbose_name_plural': 'Segundo Registro',
            },
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('importe_total', models.DecimalField(max_digits=10, decimal_places=2)),
                ('efectivo', models.DecimalField(max_digits=10, decimal_places=2)),
                ('comision', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('numero_credito', models.CharField(max_length=10)),
                ('cliente', models.ForeignKey(to='app.PrimerRegistro')),
                ('compra', models.ForeignKey(to='app.Compras')),
            ],
            options={
                'verbose_name_plural': 'Tercer Registro',
            },
        ),
        migrations.AddField(
            model_name='asesor',
            name='sucursal',
            field=models.OneToOneField(to='app.Sucursales'),
        ),
    ]
