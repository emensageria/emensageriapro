# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s5012', '0016_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s5012infocrcontrib',
            options={'managed': True, 'ordering': ['s5012_evtirrf', 'tpcr', 'vrcr'], 'permissions': (('can_see_list_s5012infoCRContrib', 'Pode ver listagem do modelo S5012INFOCRCONTRIB'), ('can_see_data_s5012infoCRContrib', 'Pode visualizar o conte\xfado do modelo S5012INFOCRCONTRIB'), ('can_see_menu_s5012infoCRContrib', 'Pode visualizar no menu o modelo S5012INFOCRCONTRIB'), ('can_print_list_s5012infoCRContrib', 'Pode imprimir listagem do modelo S5012INFOCRCONTRIB'), ('can_print_data_s5012infoCRContrib', 'Pode imprimir o conte\xfado do modelo S5012INFOCRCONTRIB'))},
        ),
    ]
