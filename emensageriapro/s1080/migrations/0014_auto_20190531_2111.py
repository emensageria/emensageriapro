# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1080', '0013_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1080alteracao',
            options={'managed': True, 'ordering': ['s1080_evttaboperport', 'cnpjopportuario', 'inivalid', 'aliqrat', 'fap', 'aliqratajust'], 'permissions': (('can_view_s1080alteracao', 'Can view S1080ALTERACAO'), ('can_view_menu_s1080alteracao', 'Can view menu S1080ALTERACAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1080alteracaonovavalidade',
            options={'managed': True, 'ordering': ['s1080_alteracao', 'inivalid'], 'permissions': (('can_view_s1080alteracaonovaValidade', 'Can view S1080ALTERACAONOVAVALIDADE'), ('can_view_menu_s1080alteracaonovaValidade', 'Can view menu S1080ALTERACAONOVAVALIDADE'))},
        ),
        migrations.AlterModelOptions(
            name='s1080exclusao',
            options={'managed': True, 'ordering': ['s1080_evttaboperport', 'cnpjopportuario', 'inivalid'], 'permissions': (('can_view_s1080exclusao', 'Can view S1080EXCLUSAO'), ('can_view_menu_s1080exclusao', 'Can view menu S1080EXCLUSAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1080inclusao',
            options={'managed': True, 'ordering': ['s1080_evttaboperport', 'cnpjopportuario', 'inivalid', 'aliqrat', 'fap', 'aliqratajust'], 'permissions': (('can_view_s1080inclusao', 'Can view S1080INCLUSAO'), ('can_view_menu_s1080inclusao', 'Can view menu S1080INCLUSAO'))},
        ),
    ]
