# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2230', '0005_auto_20190202_1446'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2230emitente',
            options={'managed': True, 'ordering': ['s2230_infoatestado', 'nmemit', 'ideoc', 'nroc'], 'permissions': (('can_view_s2230_emitente', 'Can view s2230_emitente'),)},
        ),
        migrations.AlterModelOptions(
            name='s2230fimafastamento',
            options={'managed': True, 'ordering': ['s2230_evtafasttemp', 'dttermafast'], 'permissions': (('can_view_s2230_fimafastamento', 'Can view s2230_fimafastamento'),)},
        ),
        migrations.AlterModelOptions(
            name='s2230infoatestado',
            options={'managed': True, 'ordering': ['s2230_iniafastamento', 'qtddiasafast'], 'permissions': (('can_view_s2230_infoatestado', 'Can view s2230_infoatestado'),)},
        ),
        migrations.AlterModelOptions(
            name='s2230infocessao',
            options={'managed': True, 'ordering': ['s2230_iniafastamento', 'cnpjcess', 'infonus'], 'permissions': (('can_view_s2230_infocessao', 'Can view s2230_infocessao'),)},
        ),
        migrations.AlterModelOptions(
            name='s2230infomandsind',
            options={'managed': True, 'ordering': ['s2230_iniafastamento', 'cnpjsind', 'infonusremun'], 'permissions': (('can_view_s2230_infomandsind', 'Can view s2230_infomandsind'),)},
        ),
        migrations.AlterModelOptions(
            name='s2230inforetif',
            options={'managed': True, 'ordering': ['s2230_evtafasttemp', 'origretif'], 'permissions': (('can_view_s2230_inforetif', 'Can view s2230_inforetif'),)},
        ),
        migrations.AlterModelOptions(
            name='s2230iniafastamento',
            options={'managed': True, 'ordering': ['s2230_evtafasttemp', 'dtiniafast', 'codmotafast'], 'permissions': (('can_view_s2230_iniafastamento', 'Can view s2230_iniafastamento'),)},
        ),
    ]
