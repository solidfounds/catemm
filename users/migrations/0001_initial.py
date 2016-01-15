# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('username', models.CharField(unique=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=2, choices=[('1', 'Asesor'), ('2', 'Asistente')])),
                ('porcentaje_ganancia', models.CharField(max_length=1, choices=[('3', '3%'), ('4', '4%'), ('5', '5%'), ('6', '6%')])),
                ('clave', models.CharField(max_length=10)),
                ('num_de_cuenta', models.CharField(max_length=20)),
                ('banco', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_name='user_set', related_query_name='user', verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', blank=True, to='auth.Group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
        migrations.AddField(
            model_name='user',
            name='sucursal',
            field=models.ForeignKey(null=True, to='users.Sucursal', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(related_name='user_set', related_query_name='user', verbose_name='user permissions', help_text='Specific permissions for this user.', blank=True, to='auth.Permission'),
        ),
    ]
