# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-18 22:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r4040', '0009_auto_20190620_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r4040idenat',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r4040idenat',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r4040idenat',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r4040idenat',
            name='r4040_evtbenefnid',
        ),
        migrations.RemoveField(
            model_name='r4040infopgto',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r4040infopgto',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r4040infopgto',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r4040infopgto',
            name='r4040_idenat',
        ),
        migrations.DeleteModel(
            name='r4040ideNat',
        ),
        migrations.DeleteModel(
            name='r4040infoPgto',
        ),
    ]
