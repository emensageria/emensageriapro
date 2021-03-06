# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s5013', '0004_auto_20190202_1538'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s5013baseperante',
            options={'managed': True, 'ordering': ['s5013_infobaseperante', 'tpvalore', 'basefgtse'], 'permissions': (('can_view_s5013_baseperante', 'Can view s5013_baseperante'),)},
        ),
        migrations.AlterModelOptions(
            name='s5013baseperapur',
            options={'managed': True, 'ordering': ['s5013_evtfgts', 'tpvalor', 'basefgts'], 'permissions': (('can_view_s5013_baseperapur', 'Can view s5013_baseperapur'),)},
        ),
        migrations.AlterModelOptions(
            name='s5013dpsperante',
            options={'managed': True, 'ordering': ['s5013_infodpsperante', 'tpdpse', 'vrfgtse'], 'permissions': (('can_view_s5013_dpsperante', 'Can view s5013_dpsperante'),)},
        ),
        migrations.AlterModelOptions(
            name='s5013dpsperapur',
            options={'managed': True, 'ordering': ['s5013_evtfgts', 'tpdps', 'vrfgts'], 'permissions': (('can_view_s5013_dpsperapur', 'Can view s5013_dpsperapur'),)},
        ),
        migrations.AlterModelOptions(
            name='s5013infobaseperante',
            options={'managed': True, 'ordering': ['s5013_evtfgts', 'perref'], 'permissions': (('can_view_s5013_infobaseperante', 'Can view s5013_infobaseperante'),)},
        ),
        migrations.AlterModelOptions(
            name='s5013infodpsperante',
            options={'managed': True, 'ordering': ['s5013_evtfgts', 'perref'], 'permissions': (('can_view_s5013_infodpsperante', 'Can view s5013_infodpsperante'),)},
        ),
    ]
