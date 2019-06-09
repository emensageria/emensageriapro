# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1250', '0014_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1250ideprodutor',
            options={'managed': True, 'ordering': ['s1250_tpaquis', 'tpinscprod', 'nrinscprod', 'vlrbruto', 'vrcpdescpr', 'vrratdescpr', 'vrsenardesc', 'indopccp'], 'permissions': (('can_see_list_s1250ideProdutor', 'Pode ver listagem do modelo S1250IDEPRODUTOR'), ('can_see_data_s1250ideProdutor', 'Pode visualizar o conte\xfado do modelo S1250IDEPRODUTOR'), ('can_see_menu_s1250ideProdutor', 'Pode visualizar no menu o modelo S1250IDEPRODUTOR'), ('can_print_list_s1250ideProdutor', 'Pode imprimir listagem do modelo S1250IDEPRODUTOR'), ('can_print_data_s1250ideProdutor', 'Pode imprimir o conte\xfado do modelo S1250IDEPRODUTOR'))},
        ),
        migrations.AlterModelOptions(
            name='s1250infoprocj',
            options={'managed': True, 'ordering': ['s1250_tpaquis', 'nrprocjud', 'codsusp', 'vrcpnret', 'vrratnret', 'vrsenarnret'], 'permissions': (('can_see_list_s1250infoProcJ', 'Pode ver listagem do modelo S1250INFOPROCJ'), ('can_see_data_s1250infoProcJ', 'Pode visualizar o conte\xfado do modelo S1250INFOPROCJ'), ('can_see_menu_s1250infoProcJ', 'Pode visualizar no menu o modelo S1250INFOPROCJ'), ('can_print_list_s1250infoProcJ', 'Pode imprimir listagem do modelo S1250INFOPROCJ'), ('can_print_data_s1250infoProcJ', 'Pode imprimir o conte\xfado do modelo S1250INFOPROCJ'))},
        ),
        migrations.AlterModelOptions(
            name='s1250infoprocjud',
            options={'managed': True, 'ordering': ['s1250_ideprodutor', 'nrprocjud', 'codsusp', 'vrcpnret', 'vrratnret', 'vrsenarnret'], 'permissions': (('can_see_list_s1250infoProcJud', 'Pode ver listagem do modelo S1250INFOPROCJUD'), ('can_see_data_s1250infoProcJud', 'Pode visualizar o conte\xfado do modelo S1250INFOPROCJUD'), ('can_see_menu_s1250infoProcJud', 'Pode visualizar no menu o modelo S1250INFOPROCJUD'), ('can_print_list_s1250infoProcJud', 'Pode imprimir listagem do modelo S1250INFOPROCJUD'), ('can_print_data_s1250infoProcJud', 'Pode imprimir o conte\xfado do modelo S1250INFOPROCJUD'))},
        ),
        migrations.AlterModelOptions(
            name='s1250nfs',
            options={'managed': True, 'ordering': ['s1250_ideprodutor', 'nrdocto', 'dtemisnf', 'vlrbruto', 'vrcpdescpr', 'vrratdescpr', 'vrsenardesc'], 'permissions': (('can_see_list_s1250nfs', 'Pode ver listagem do modelo S1250NFS'), ('can_see_data_s1250nfs', 'Pode visualizar o conte\xfado do modelo S1250NFS'), ('can_see_menu_s1250nfs', 'Pode visualizar no menu o modelo S1250NFS'), ('can_print_list_s1250nfs', 'Pode imprimir listagem do modelo S1250NFS'), ('can_print_data_s1250nfs', 'Pode imprimir o conte\xfado do modelo S1250NFS'))},
        ),
        migrations.AlterModelOptions(
            name='s1250tpaquis',
            options={'managed': True, 'ordering': ['s1250_evtaqprod', 'indaquis', 'vlrtotaquis'], 'permissions': (('can_see_list_s1250tpAquis', 'Pode ver listagem do modelo S1250TPAQUIS'), ('can_see_data_s1250tpAquis', 'Pode visualizar o conte\xfado do modelo S1250TPAQUIS'), ('can_see_menu_s1250tpAquis', 'Pode visualizar no menu o modelo S1250TPAQUIS'), ('can_print_list_s1250tpAquis', 'Pode imprimir listagem do modelo S1250TPAQUIS'), ('can_print_data_s1250tpAquis', 'Pode imprimir o conte\xfado do modelo S1250TPAQUIS'))},
        ),
    ]