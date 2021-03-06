# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r2020', '0015_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='r2020infoprocretad',
            options={'managed': True, 'ordering': ['r2020_evtservprest', 'tpprocretadic', 'nrprocretadic', 'valoradic'], 'permissions': (('can_see_list_r2020infoProcRetAd', 'Pode ver listagem do modelo R2020INFOPROCRETAD'), ('can_see_data_r2020infoProcRetAd', 'Pode visualizar o conte\xfado do modelo R2020INFOPROCRETAD'), ('can_see_menu_r2020infoProcRetAd', 'Pode visualizar no menu o modelo R2020INFOPROCRETAD'), ('can_print_list_r2020infoProcRetAd', 'Pode imprimir listagem do modelo R2020INFOPROCRETAD'), ('can_print_data_r2020infoProcRetAd', 'Pode imprimir o conte\xfado do modelo R2020INFOPROCRETAD'))},
        ),
        migrations.AlterModelOptions(
            name='r2020infoprocretpr',
            options={'managed': True, 'ordering': ['r2020_evtservprest', 'tpprocretprinc', 'nrprocretprinc', 'valorprinc'], 'permissions': (('can_see_list_r2020infoProcRetPr', 'Pode ver listagem do modelo R2020INFOPROCRETPR'), ('can_see_data_r2020infoProcRetPr', 'Pode visualizar o conte\xfado do modelo R2020INFOPROCRETPR'), ('can_see_menu_r2020infoProcRetPr', 'Pode visualizar no menu o modelo R2020INFOPROCRETPR'), ('can_print_list_r2020infoProcRetPr', 'Pode imprimir listagem do modelo R2020INFOPROCRETPR'), ('can_print_data_r2020infoProcRetPr', 'Pode imprimir o conte\xfado do modelo R2020INFOPROCRETPR'))},
        ),
        migrations.AlterModelOptions(
            name='r2020infotpserv',
            options={'managed': True, 'ordering': ['r2020_nfs', 'tpservico', 'vlrbaseret', 'vlrretencao'], 'permissions': (('can_see_list_r2020infoTpServ', 'Pode ver listagem do modelo R2020INFOTPSERV'), ('can_see_data_r2020infoTpServ', 'Pode visualizar o conte\xfado do modelo R2020INFOTPSERV'), ('can_see_menu_r2020infoTpServ', 'Pode visualizar no menu o modelo R2020INFOTPSERV'), ('can_print_list_r2020infoTpServ', 'Pode imprimir listagem do modelo R2020INFOTPSERV'), ('can_print_data_r2020infoTpServ', 'Pode imprimir o conte\xfado do modelo R2020INFOTPSERV'))},
        ),
        migrations.AlterModelOptions(
            name='r2020nfs',
            options={'managed': True, 'ordering': ['r2020_evtservprest', 'serie', 'numdocto', 'dtemissaonf', 'vlrbruto'], 'permissions': (('can_see_list_r2020nfs', 'Pode ver listagem do modelo R2020NFS'), ('can_see_data_r2020nfs', 'Pode visualizar o conte\xfado do modelo R2020NFS'), ('can_see_menu_r2020nfs', 'Pode visualizar no menu o modelo R2020NFS'), ('can_print_list_r2020nfs', 'Pode imprimir listagem do modelo R2020NFS'), ('can_print_data_r2020nfs', 'Pode imprimir o conte\xfado do modelo R2020NFS'))},
        ),
    ]
