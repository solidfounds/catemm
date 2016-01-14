# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status', default=False)),
                ('username', models.CharField(max_length=100, unique=True)),
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
                ('groups', models.ManyToManyField(to='auth.Group', related_name='user_set', related_query_name='user', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', blank=True)),
                ('sucursal', models.ForeignKey(to='app.Sucursales')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', related_name='user_set', related_query_name='user', help_text='Specific permissions for this user.', verbose_name='user permissions', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
