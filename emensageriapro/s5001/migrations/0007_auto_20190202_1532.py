# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-02 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s5001', '0006_auto_20181213_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s5001calcterc',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5001ideestablot',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5001infobasecs',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5001infocategincid',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5001infocpcalc',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='s5001procjudtrab',
            name='excluido',
            field=models.NullBooleanField(default=False),
        ),
    ]
