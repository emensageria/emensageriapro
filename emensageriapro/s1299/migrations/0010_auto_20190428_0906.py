# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-28 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s1299', '0009_auto_20190427_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s1299iderespinf',
            name='cpfresp',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='s1299iderespinf',
            name='nmresp',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='s1299iderespinf',
            name='s1299_evtfechaevper',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='s1299iderespinf_s1299_evtfechaevper', to='esocial.s1299evtFechaEvPer'),
        ),
        migrations.AlterField(
            model_name='s1299iderespinf',
            name='telefone',
            field=models.CharField(max_length=13),
        ),
    ]
