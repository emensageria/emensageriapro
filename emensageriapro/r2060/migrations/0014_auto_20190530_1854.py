# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('r2060', '0013_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r2060tipocod',
            name='codativecon',
            field=models.TextField(null=True),
        ),
    ]
