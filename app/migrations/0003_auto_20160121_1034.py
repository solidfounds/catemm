# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160120_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComisionEmpleados',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('monto', models.DecimalField(max_digits=7, decimal_places=2)),
                ('liquidado', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Comisión Empleados',
            },
        ),
        migrations.AlterField(
            model_name='primerregistro',
            name='comision',
            field=models.DecimalField(max_digits=7, decimal_places=2, verbose_name='comisión'),
        ),
        migrations.AlterField(
            model_name='primerregistro',
            name='direccion',
            field=models.TextField(verbose_name='dirección'),
        ),
        migrations.AlterField(
            model_name='primerregistro',
            name='numero_de_cuenta',
            field=models.CharField(verbose_name='número de cuenta', max_length=16),
        ),
        migrations.AlterField(
            model_name='primerregistro',
            name='telefono',
            field=models.SmallIntegerField(verbose_name='teléfono'),
        ),
        migrations.AlterField(
            model_name='segundoregistro',
            name='caratula',
            field=models.CharField(verbose_name='carátula', max_length=50),
        ),
        migrations.AlterField(
            model_name='segundoregistro',
            name='credito',
            field=models.DecimalField(max_digits=7, null=True, verbose_name='crédito', blank=True, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='segundoregistro',
            name='numero_tarjeta',
            field=models.SmallIntegerField(verbose_name='número de tarjeta'),
        ),
        migrations.AddField(
            model_name='comisionempleados',
            name='cliente',
            field=models.ForeignKey(to='app.SegundoRegistro'),
        ),
    ]
