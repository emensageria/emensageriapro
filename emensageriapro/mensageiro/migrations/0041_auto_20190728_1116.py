# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-28 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0040_auto_20190728_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transmissorlote',
            name='nrinsc',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='transmissorlote',
            name='transmissor_nrinsc',
            field=models.CharField(max_length=15),
        ),
    ]
