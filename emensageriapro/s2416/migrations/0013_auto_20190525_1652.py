# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-25 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s2416', '0012_auto_20190514_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2416homologtc',
            name='nratolegal',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='s2416infopenmorte',
            name='tppenmorte',
            field=models.IntegerField(choices=[(1, '1 - Vital\xedcia'), (2, '2 - Tempor\xe1ria.')], null=True),
        ),
        migrations.AlterField(
            model_name='s2416suspensao',
            name='mtvsuspensao',
            field=models.CharField(choices=[(b'01', '01 - Suspens\xe3o por n\xe3o recadastramento'), (b'99', '99 - Outros motivos de suspens\xe3o.')], max_length=2, null=True),
        ),
    ]