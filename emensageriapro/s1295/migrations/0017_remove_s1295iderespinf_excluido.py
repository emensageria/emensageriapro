# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle_de_acesso', '0026_auto_20190620_1505'),
        ('s1295', '0016_auto_20190620_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s1295iderespinf',
            name='excluido',
        ),
    ]