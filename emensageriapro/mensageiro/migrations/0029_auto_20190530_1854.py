# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0028_auto_20190529_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retornoseventos',
            name='empregador_tpinsc',
            field=models.IntegerField(blank=True, choices=[(1, '1 - CNPJ'), (2, '2 - CPF.')], null=True),
        ),
        migrations.AlterField(
            model_name='retornoseventos',
            name='local_tpinsc',
            field=models.IntegerField(blank=True, choices=[(1, '1 - CNPJ'), (2, '2 - CPF.')], null=True),
        ),
        migrations.AlterField(
            model_name='retornoseventos',
            name='tpinsc',
            field=models.IntegerField(blank=True, choices=[(1, '1 - CNPJ'), (2, '2 - CPF.')], null=True),
        ),
    ]
