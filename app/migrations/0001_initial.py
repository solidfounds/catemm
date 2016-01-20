# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta_',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('cantidad', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrimerRegistro',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
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
            name='Productos',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.SmallIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Productos',
                'verbose_name': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='SegundoRegistro',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('caratula', models.CharField(max_length=50)),
                ('tarjeta_de_mejoravit', models.FileField(upload_to='media/targeta_infonavit')),
                ('numero_tarjeta', models.SmallIntegerField()),
                ('tarjeta_entregada', models.BooleanField()),
                ('tarjeta_activa', models.BooleanField()),
                ('tarjeta_con_fondos', models.BooleanField()),
                ('credito', models.DecimalField(decimal_places=2, null=True, blank=True, max_digits=7)),
                ('cliente', models.ForeignKey(to='app.PrimerRegistro')),
            ],
            options={
                'verbose_name_plural': 'Segundo Registro',
            },
        ),
        migrations.CreateModel(
            name='TercerRegistro',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
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
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(verbose_name='Total', decimal_places=2, default=0, max_digits=9, blank=True, null=True)),
                ('cliente', models.ForeignKey(to='app.PrimerRegistro')),
                ('detalle_venta', models.ManyToManyField(to='app.Productos')),
            ],
        ),
    ]
