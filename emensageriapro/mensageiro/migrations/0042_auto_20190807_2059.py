# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-07 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0041_auto_20190728_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='transmissorloteefdreinf',
            name='data_hora_consulta',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transmissorloteefdreinf',
            name='data_hora_envio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transmissorloteesocial',
            name='data_hora_consulta',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transmissorloteesocial',
            name='data_hora_envio',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]