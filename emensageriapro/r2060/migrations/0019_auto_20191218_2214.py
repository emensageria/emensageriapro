# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-18 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r2060', '0018_auto_20190620_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r2060tipocod',
            name='observ',
        ),
        migrations.AlterField(
            model_name='r2060tipoajuste',
            name='tpajuste',
            field=models.IntegerField(choices=[(0, '0 - Ajuste de redu\xe7\xe3o'), (1, '1 - Ajuste de acr\xe9scimo')], null=True),
        ),
    ]