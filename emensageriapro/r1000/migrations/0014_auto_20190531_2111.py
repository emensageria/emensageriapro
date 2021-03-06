# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-31 21:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r1000', '0013_auto_20190525_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r1000alteracao',
            options={'managed': True, 'ordering': ['r1000_evtinfocontri', 'inivalid', 'classtrib', 'indescrituracao', 'inddesoneracao', 'indacordoisenmulta', 'nmctt', 'cpfctt'], 'permissions': (('can_view_r1000alteracao', 'Can view R1000ALTERACAO'), ('can_view_menu_r1000alteracao', 'Can view menu R1000ALTERACAO'))},
        ),
        migrations.AlterModelOptions(
            name='r1000alteracaoinfoefr',
            options={'managed': True, 'ordering': ['r1000_alteracao', 'ideefr'], 'permissions': (('can_view_r1000alteracaoinfoEFR', 'Can view R1000ALTERACAOINFOEFR'), ('can_view_menu_r1000alteracaoinfoEFR', 'Can view menu R1000ALTERACAOINFOEFR'))},
        ),
        migrations.AlterModelOptions(
            name='r1000alteracaonovavalidade',
            options={'managed': True, 'ordering': ['r1000_alteracao', 'inivalid'], 'permissions': (('can_view_r1000alteracaonovaValidade', 'Can view R1000ALTERACAONOVAVALIDADE'), ('can_view_menu_r1000alteracaonovaValidade', 'Can view menu R1000ALTERACAONOVAVALIDADE'))},
        ),
        migrations.AlterModelOptions(
            name='r1000alteracaosofthouse',
            options={'managed': True, 'ordering': ['r1000_alteracao', 'cnpjsofthouse', 'nmrazao', 'nmcont'], 'permissions': (('can_view_r1000alteracaosoftHouse', 'Can view R1000ALTERACAOSOFTHOUSE'), ('can_view_menu_r1000alteracaosoftHouse', 'Can view menu R1000ALTERACAOSOFTHOUSE'))},
        ),
        migrations.AlterModelOptions(
            name='r1000exclusao',
            options={'managed': True, 'ordering': ['r1000_evtinfocontri', 'inivalid'], 'permissions': (('can_view_r1000exclusao', 'Can view R1000EXCLUSAO'), ('can_view_menu_r1000exclusao', 'Can view menu R1000EXCLUSAO'))},
        ),
        migrations.AlterModelOptions(
            name='r1000inclusao',
            options={'managed': True, 'ordering': ['r1000_evtinfocontri', 'inivalid', 'classtrib', 'indescrituracao', 'inddesoneracao', 'indacordoisenmulta', 'nmctt', 'cpfctt'], 'permissions': (('can_view_r1000inclusao', 'Can view R1000INCLUSAO'), ('can_view_menu_r1000inclusao', 'Can view menu R1000INCLUSAO'))},
        ),
        migrations.AlterModelOptions(
            name='r1000inclusaoinfoefr',
            options={'managed': True, 'ordering': ['r1000_inclusao', 'ideefr'], 'permissions': (('can_view_r1000inclusaoinfoEFR', 'Can view R1000INCLUSAOINFOEFR'), ('can_view_menu_r1000inclusaoinfoEFR', 'Can view menu R1000INCLUSAOINFOEFR'))},
        ),
        migrations.AlterModelOptions(
            name='r1000inclusaosofthouse',
            options={'managed': True, 'ordering': ['r1000_inclusao', 'cnpjsofthouse', 'nmrazao', 'nmcont'], 'permissions': (('can_view_r1000inclusaosoftHouse', 'Can view R1000INCLUSAOSOFTHOUSE'), ('can_view_menu_r1000inclusaosoftHouse', 'Can view menu R1000INCLUSAOSOFTHOUSE'))},
        ),
    ]
