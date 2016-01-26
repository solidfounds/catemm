# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160121_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=250)),
                ('order_date', models.DateTimeField(verbose_name='date', auto_now_add=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(to='app.PrimerRegistro')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(to='app.Order')),
                ('product', models.ForeignKey(to='app.Productos')),
            ],
        ),
        migrations.RemoveField(
            model_name='detalleventa_',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='detalleventa_',
            name='venta',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='detalle_venta',
        ),
        migrations.DeleteModel(
            name='DetalleVenta_',
        ),
        migrations.DeleteModel(
            name='Venta',
        ),
    ]
