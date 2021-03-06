# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r4040', '0006_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r4040idenat',
            options={'managed': True, 'ordering': ['r4040_evtbenefnid', 'natrendim'], 'permissions': (('can_see_list_r4040ideNat', 'Pode ver listagem do modelo R4040IDENAT'), ('can_see_data_r4040ideNat', 'Pode visualizar o conte\xfado do modelo R4040IDENAT'), ('can_see_menu_r4040ideNat', 'Pode visualizar no menu o modelo R4040IDENAT'), ('can_print_list_r4040ideNat', 'Pode imprimir listagem do modelo R4040IDENAT'), ('can_print_data_r4040ideNat', 'Pode imprimir o conte\xfado do modelo R4040IDENAT'))},
        ),
        migrations.AlterModelOptions(
            name='r4040infopgto',
            options={'managed': True, 'ordering': ['r4040_idenat', 'dtfg', 'vlrliq', 'vlrreaj', 'vlrir', 'descr'], 'permissions': (('can_see_list_r4040infoPgto', 'Pode ver listagem do modelo R4040INFOPGTO'), ('can_see_data_r4040infoPgto', 'Pode visualizar o conte\xfado do modelo R4040INFOPGTO'), ('can_see_menu_r4040infoPgto', 'Pode visualizar no menu o modelo R4040INFOPGTO'), ('can_print_list_r4040infoPgto', 'Pode imprimir listagem do modelo R4040INFOPGTO'), ('can_print_data_r4040infoPgto', 'Pode imprimir o conte\xfado do modelo R4040INFOPGTO'))},
        ),
    ]
