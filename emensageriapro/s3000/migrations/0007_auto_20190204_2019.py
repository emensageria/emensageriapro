# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s3000', '0006_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s3000idefolhapagto',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s3000idefolhapagto',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s3000idetrabalhador',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s3000idetrabalhador',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='s3000idefolhapagto',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s3000idefolhapagto',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s3000idetrabalhador',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s3000idetrabalhador',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]