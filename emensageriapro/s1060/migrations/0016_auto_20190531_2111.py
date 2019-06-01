# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1060', '0015_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1060alteracao',
            options={'managed': True, 'ordering': ['s1060_evttabambiente', 'codamb', 'inivalid', 'nmamb', 'dscamb', 'localamb'], 'permissions': (('can_view_s1060alteracao', 'Can view S1060ALTERACAO'), ('can_view_menu_s1060alteracao', 'Can view menu S1060ALTERACAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1060alteracaonovavalidade',
            options={'managed': True, 'ordering': ['s1060_alteracao', 'inivalid'], 'permissions': (('can_view_s1060alteracaonovaValidade', 'Can view S1060ALTERACAONOVAVALIDADE'), ('can_view_menu_s1060alteracaonovaValidade', 'Can view menu S1060ALTERACAONOVAVALIDADE'))},
        ),
        migrations.AlterModelOptions(
            name='s1060exclusao',
            options={'managed': True, 'ordering': ['s1060_evttabambiente', 'codamb', 'inivalid'], 'permissions': (('can_view_s1060exclusao', 'Can view S1060EXCLUSAO'), ('can_view_menu_s1060exclusao', 'Can view menu S1060EXCLUSAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1060inclusao',
            options={'managed': True, 'ordering': ['s1060_evttabambiente', 'codamb', 'inivalid', 'nmamb', 'dscamb', 'localamb'], 'permissions': (('can_view_s1060inclusao', 'Can view S1060INCLUSAO'), ('can_view_menu_s1060inclusao', 'Can view menu S1060INCLUSAO'))},
        ),
    ]