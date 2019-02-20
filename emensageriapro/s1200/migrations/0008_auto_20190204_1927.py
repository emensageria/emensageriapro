# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1200', '0007_auto_20190202_1246'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1200dmdev',
            options={'managed': True, 'ordering': ['s1200_evtremun', 'idedmdev', 'codcateg'], 'permissions': (('can_view_s1200_dmdev', 'Can view s1200_dmdev'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infocomplem',
            options={'managed': True, 'ordering': ['s1200_evtremun', 'nmtrab', 'dtnascto'], 'permissions': (('can_view_s1200_infocomplem', 'Can view s1200_infocomplem'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infointerm',
            options={'managed': True, 'ordering': ['s1200_evtremun', 'qtddiasinterm'], 'permissions': (('can_view_s1200_infointerm', 'Can view s1200_infointerm'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infomv',
            options={'managed': True, 'ordering': ['s1200_evtremun', 'indmv'], 'permissions': (('can_view_s1200_infomv', 'Can view s1200_infomv'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperantideadc',
            options={'managed': True, 'ordering': ['s1200_dmdev', 'tpacconv', 'dsc', 'remunsuc'], 'permissions': (('can_view_s1200_infoperant_ideadc', 'Can view s1200_infoperant_ideadc'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperantideestablot',
            options={'managed': True, 'ordering': ['s1200_infoperant_ideperiodo', 'tpinsc', 'nrinsc', 'codlotacao'], 'permissions': (('can_view_s1200_infoperant_ideestablot', 'Can view s1200_infoperant_ideestablot'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperantideperiodo',
            options={'managed': True, 'ordering': ['s1200_infoperant_ideadc', 'perref'], 'permissions': (('can_view_s1200_infoperant_ideperiodo', 'Can view s1200_infoperant_ideperiodo'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperantinfoagnocivo',
            options={'managed': True, 'ordering': ['s1200_infoperant_remunperant', 'grauexp'], 'permissions': (('can_view_s1200_infoperant_infoagnocivo', 'Can view s1200_infoperant_infoagnocivo'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperantinfocomplcont',
            options={'managed': True, 'ordering': ['s1200_dmdev', 'codcbo'], 'permissions': (('can_view_s1200_infoperant_infocomplcont', 'Can view s1200_infoperant_infocomplcont'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperantinfotrabinterm',
            options={'managed': True, 'ordering': ['s1200_infoperant_remunperant', 'codconv'], 'permissions': (('can_view_s1200_infoperant_infotrabinterm', 'Can view s1200_infoperant_infotrabinterm'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperantitensremun',
            options={'managed': True, 'ordering': ['s1200_infoperant_remunperant', 'codrubr', 'idetabrubr', 'vrrubr'], 'permissions': (('can_view_s1200_infoperant_itensremun', 'Can view s1200_infoperant_itensremun'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperantremunperant',
            options={'managed': True, 'ordering': ['s1200_infoperant_ideestablot'], 'permissions': (('can_view_s1200_infoperant_remunperant', 'Can view s1200_infoperant_remunperant'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperapurdetoper',
            options={'managed': True, 'ordering': ['s1200_infoperapur_remunperapur', 'cnpjoper', 'regans', 'vrpgtit'], 'permissions': (('can_view_s1200_infoperapur_detoper', 'Can view s1200_infoperapur_detoper'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperapurdetplano',
            options={'managed': True, 'ordering': ['s1200_infoperapur_detoper', 'tpdep', 'nmdep', 'dtnascto', 'vlrpgdep'], 'permissions': (('can_view_s1200_infoperapur_detplano', 'Can view s1200_infoperapur_detplano'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperapurideestablot',
            options={'managed': True, 'ordering': ['s1200_dmdev', 'tpinsc', 'nrinsc', 'codlotacao'], 'permissions': (('can_view_s1200_infoperapur_ideestablot', 'Can view s1200_infoperapur_ideestablot'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperapurinfoagnocivo',
            options={'managed': True, 'ordering': ['s1200_infoperapur_remunperapur', 'grauexp'], 'permissions': (('can_view_s1200_infoperapur_infoagnocivo', 'Can view s1200_infoperapur_infoagnocivo'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperapurinfotrabinterm',
            options={'managed': True, 'ordering': ['s1200_infoperapur_remunperapur', 'codconv'], 'permissions': (('can_view_s1200_infoperapur_infotrabinterm', 'Can view s1200_infoperapur_infotrabinterm'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperapuritensremun',
            options={'managed': True, 'ordering': ['s1200_infoperapur_remunperapur', 'codrubr', 'idetabrubr', 'vrrubr'], 'permissions': (('can_view_s1200_infoperapur_itensremun', 'Can view s1200_infoperapur_itensremun'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200infoperapurremunperapur',
            options={'managed': True, 'ordering': ['s1200_infoperapur_ideestablot'], 'permissions': (('can_view_s1200_infoperapur_remunperapur', 'Can view s1200_infoperapur_remunperapur'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200procjudtrab',
            options={'managed': True, 'ordering': ['s1200_evtremun', 'tptrib', 'nrprocjud'], 'permissions': (('can_view_s1200_procjudtrab', 'Can view s1200_procjudtrab'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200remunoutrempr',
            options={'managed': True, 'ordering': ['s1200_infomv', 'tpinsc', 'nrinsc', 'codcateg', 'vlrremunoe'], 'permissions': (('can_view_s1200_remunoutrempr', 'Can view s1200_remunoutrempr'),)},
        ),
        migrations.AlterModelOptions(
            name='s1200sucessaovinc',
            options={'managed': True, 'ordering': ['s1200_infocomplem', 'tpinscant', 'cnpjempregant', 'dtadm'], 'permissions': (('can_view_s1200_sucessaovinc', 'Can view s1200_sucessaovinc'),)},
        ),
    ]