# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_relacionp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relacionp',
            name='com_t',
            field=models.DecimalField(max_digits=7, verbose_name='Comisón Total', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='relacionp',
            name='comision',
            field=models.DecimalField(max_digits=7, verbose_name='Comisión', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='relacionp',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='relacionp',
            name='importe',
            field=models.DecimalField(max_digits=7, verbose_name='Importe', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='relacionp',
            name='odc1',
            field=models.DecimalField(max_digits=7, verbose_name='Ordende Compra 1', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='relacionp',
            name='odc2',
            field=models.DecimalField(max_digits=7, verbose_name='Orden de Compra 2', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='relacionp',
            name='odc3',
            field=models.DecimalField(max_digits=7, verbose_name='Orden de Compra 3', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='relacionp',
            name='p_asesor',
            field=models.DecimalField(max_digits=7, verbose_name='% Asesor', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='relacionp',
            name='pag_clie',
            field=models.DecimalField(max_digits=7, verbose_name='Pago Cliente', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='relacionp',
            name='ref_pago',
            field=models.CharField(max_length=20, verbose_name='Referencia de Pago'),
        ),
    ]
