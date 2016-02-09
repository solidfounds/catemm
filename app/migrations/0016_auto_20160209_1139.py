# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20160208_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primerregistro',
            name='comision',
            field=models.DecimalField(verbose_name=b'comisi\xc3\xb3n', max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='primerregistro',
            name='direccion',
            field=models.TextField(verbose_name=b'direcci\xc3\xb3n'),
        ),
        migrations.AlterField(
            model_name='primerregistro',
            name='numero_de_cuenta',
            field=models.CharField(max_length=16, verbose_name=b'n\xc3\xbamero de cuenta'),
        ),
        migrations.AlterField(
            model_name='primerregistro',
            name='telefono',
            field=models.PositiveIntegerField(verbose_name=b'tel\xc3\xa9fono'),
        ),
        migrations.AlterField(
            model_name='relacionp',
            name='com_t',
            field=models.DecimalField(verbose_name=b'Comis\xc3\xb3n Total', max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='relacionp',
            name='comision',
            field=models.DecimalField(verbose_name=b'Comisi\xc3\xb3n', max_digits=7, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='segundoregistro',
            name='caratula',
            field=models.CharField(max_length=50, verbose_name=b'car\xc3\xa1tula'),
        ),
        migrations.AlterField(
            model_name='segundoregistro',
            name='credito',
            field=models.DecimalField(null=True, verbose_name=b'cr\xc3\xa9dito', max_digits=7, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='segundoregistro',
            name='numero_tarjeta',
            field=models.PositiveIntegerField(verbose_name=b'n\xc3\xbamero de tarjeta'),
        ),
    ]
