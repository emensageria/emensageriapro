# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1300', '0014_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1300contribsind',
            options={'managed': True, 'ordering': ['s1300_evtcontrsindpatr', 'cnpjsindic', 'tpcontribsind', 'vlrcontribsind'], 'permissions': (('can_see_list_s1300contribSind', 'Pode ver listagem do modelo S1300CONTRIBSIND'), ('can_see_data_s1300contribSind', 'Pode visualizar o conte\xfado do modelo S1300CONTRIBSIND'), ('can_see_menu_s1300contribSind', 'Pode visualizar no menu o modelo S1300CONTRIBSIND'), ('can_print_list_s1300contribSind', 'Pode imprimir listagem do modelo S1300CONTRIBSIND'), ('can_print_data_s1300contribSind', 'Pode imprimir o conte\xfado do modelo S1300CONTRIBSIND'))},
        ),
    ]
