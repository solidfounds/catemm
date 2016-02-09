# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0013_auto_20160207_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelacionP',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('fecha', models.DateField()),
                ('odc1', models.DecimalField(max_digits=7, decimal_places=2)),
                ('odc2', models.DecimalField(max_digits=7, decimal_places=2)),
                ('odc3', models.DecimalField(max_digits=7, decimal_places=2)),
                ('pag_clie', models.DecimalField(max_digits=7, decimal_places=2)),
                ('p_asesor', models.DecimalField(max_digits=7, decimal_places=2)),
                ('comision', models.DecimalField(max_digits=7, decimal_places=2)),
                ('com_t', models.DecimalField(max_digits=7, decimal_places=2)),
                ('ref_pago', models.CharField(max_length=20)),
                ('importe', models.DecimalField(max_digits=7, decimal_places=2)),
                ('asesor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('cliente', models.ForeignKey(to='app.PrimerRegistro')),
            ],
        ),
    ]
