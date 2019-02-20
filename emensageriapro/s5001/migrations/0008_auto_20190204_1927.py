# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s5001', '0007_auto_20190202_1532'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s5001calcterc',
            options={'managed': True, 'ordering': ['s5001_infocategincid', 'tpcr', 'vrcssegterc', 'vrdescterc'], 'permissions': (('can_view_s5001_calcterc', 'Can view s5001_calcterc'),)},
        ),
        migrations.AlterModelOptions(
            name='s5001ideestablot',
            options={'managed': True, 'ordering': ['s5001_evtbasestrab', 'tpinsc', 'nrinsc', 'codlotacao'], 'permissions': (('can_view_s5001_ideestablot', 'Can view s5001_ideestablot'),)},
        ),
        migrations.AlterModelOptions(
            name='s5001infobasecs',
            options={'managed': True, 'ordering': ['s5001_infocategincid', 'ind13', 'tpvalor', 'valor'], 'permissions': (('can_view_s5001_infobasecs', 'Can view s5001_infobasecs'),)},
        ),
        migrations.AlterModelOptions(
            name='s5001infocategincid',
            options={'managed': True, 'ordering': ['s5001_ideestablot', 'codcateg'], 'permissions': (('can_view_s5001_infocategincid', 'Can view s5001_infocategincid'),)},
        ),
        migrations.AlterModelOptions(
            name='s5001infocpcalc',
            options={'managed': True, 'ordering': ['s5001_evtbasestrab', 'tpcr', 'vrcpseg', 'vrdescseg'], 'permissions': (('can_view_s5001_infocpcalc', 'Can view s5001_infocpcalc'),)},
        ),
        migrations.AlterModelOptions(
            name='s5001procjudtrab',
            options={'managed': True, 'ordering': ['s5001_evtbasestrab', 'nrprocjud', 'codsusp'], 'permissions': (('can_view_s5001_procjudtrab', 'Can view s5001_procjudtrab'),)},
        ),
    ]