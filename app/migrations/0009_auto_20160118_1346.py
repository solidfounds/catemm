# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160118_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleVenta_',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cantidad', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
                ('producto', models.ForeignKey(to='app.Productos')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(default=0, verbose_name='Total', null=True, max_digits=9, blank=True, decimal_places=2)),
                ('cliente', models.ForeignKey(to='app.PrimerRegistro')),
                ('detalle_venta', models.ManyToManyField(to='app.Productos')),
            ],
        ),
        migrations.AddField(
            model_name='detalleventa_',
            name='venta',
            field=models.ForeignKey(to='app.Venta'),
        ),
    ]
