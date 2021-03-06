# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s5003', '0014_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s5003baseperante',
            options={'managed': True, 'ordering': ['s5003_infobaseperante', 'tpvalore', 'remfgtse'], 'permissions': (('can_see_list_s5003basePerAntE', 'Pode ver listagem do modelo S5003BASEPERANTE'), ('can_see_data_s5003basePerAntE', 'Pode visualizar o conte\xfado do modelo S5003BASEPERANTE'), ('can_see_menu_s5003basePerAntE', 'Pode visualizar no menu o modelo S5003BASEPERANTE'), ('can_print_list_s5003basePerAntE', 'Pode imprimir listagem do modelo S5003BASEPERANTE'), ('can_print_data_s5003basePerAntE', 'Pode imprimir o conte\xfado do modelo S5003BASEPERANTE'))},
        ),
        migrations.AlterModelOptions(
            name='s5003baseperapur',
            options={'managed': True, 'ordering': ['s5003_infobasefgts', 'tpvalor', 'remfgts'], 'permissions': (('can_see_list_s5003basePerApur', 'Pode ver listagem do modelo S5003BASEPERAPUR'), ('can_see_data_s5003basePerApur', 'Pode visualizar o conte\xfado do modelo S5003BASEPERAPUR'), ('can_see_menu_s5003basePerApur', 'Pode visualizar no menu o modelo S5003BASEPERAPUR'), ('can_print_list_s5003basePerApur', 'Pode imprimir listagem do modelo S5003BASEPERAPUR'), ('can_print_data_s5003basePerApur', 'Pode imprimir o conte\xfado do modelo S5003BASEPERAPUR'))},
        ),
        migrations.AlterModelOptions(
            name='s5003dpsperante',
            options={'managed': True, 'ordering': ['s5003_infodpsperante', 'tpdpse', 'dpsfgtse'], 'permissions': (('can_see_list_s5003dpsPerAntE', 'Pode ver listagem do modelo S5003DPSPERANTE'), ('can_see_data_s5003dpsPerAntE', 'Pode visualizar o conte\xfado do modelo S5003DPSPERANTE'), ('can_see_menu_s5003dpsPerAntE', 'Pode visualizar no menu o modelo S5003DPSPERANTE'), ('can_print_list_s5003dpsPerAntE', 'Pode imprimir listagem do modelo S5003DPSPERANTE'), ('can_print_data_s5003dpsPerAntE', 'Pode imprimir o conte\xfado do modelo S5003DPSPERANTE'))},
        ),
        migrations.AlterModelOptions(
            name='s5003dpsperapur',
            options={'managed': True, 'ordering': ['s5003_infotrabdps', 'tpdps', 'dpsfgts'], 'permissions': (('can_see_list_s5003dpsPerApur', 'Pode ver listagem do modelo S5003DPSPERAPUR'), ('can_see_data_s5003dpsPerApur', 'Pode visualizar o conte\xfado do modelo S5003DPSPERAPUR'), ('can_see_menu_s5003dpsPerApur', 'Pode visualizar no menu o modelo S5003DPSPERAPUR'), ('can_print_list_s5003dpsPerApur', 'Pode imprimir listagem do modelo S5003DPSPERAPUR'), ('can_print_data_s5003dpsPerApur', 'Pode imprimir o conte\xfado do modelo S5003DPSPERAPUR'))},
        ),
        migrations.AlterModelOptions(
            name='s5003ideestablot',
            options={'managed': True, 'ordering': ['s5003_evtbasesfgts', 'tpinsc', 'nrinsc', 'codlotacao'], 'permissions': (('can_see_list_s5003ideEstabLot', 'Pode ver listagem do modelo S5003IDEESTABLOT'), ('can_see_data_s5003ideEstabLot', 'Pode visualizar o conte\xfado do modelo S5003IDEESTABLOT'), ('can_see_menu_s5003ideEstabLot', 'Pode visualizar no menu o modelo S5003IDEESTABLOT'), ('can_print_list_s5003ideEstabLot', 'Pode imprimir listagem do modelo S5003IDEESTABLOT'), ('can_print_data_s5003ideEstabLot', 'Pode imprimir o conte\xfado do modelo S5003IDEESTABLOT'))},
        ),
        migrations.AlterModelOptions(
            name='s5003infobasefgts',
            options={'managed': True, 'ordering': ['s5003_infotrabfgts'], 'permissions': (('can_see_list_s5003infoBaseFGTS', 'Pode ver listagem do modelo S5003INFOBASEFGTS'), ('can_see_data_s5003infoBaseFGTS', 'Pode visualizar o conte\xfado do modelo S5003INFOBASEFGTS'), ('can_see_menu_s5003infoBaseFGTS', 'Pode visualizar no menu o modelo S5003INFOBASEFGTS'), ('can_print_list_s5003infoBaseFGTS', 'Pode imprimir listagem do modelo S5003INFOBASEFGTS'), ('can_print_data_s5003infoBaseFGTS', 'Pode imprimir o conte\xfado do modelo S5003INFOBASEFGTS'))},
        ),
        migrations.AlterModelOptions(
            name='s5003infobaseperante',
            options={'managed': True, 'ordering': ['s5003_infobasefgts', 'perref'], 'permissions': (('can_see_list_s5003infoBasePerAntE', 'Pode ver listagem do modelo S5003INFOBASEPERANTE'), ('can_see_data_s5003infoBasePerAntE', 'Pode visualizar o conte\xfado do modelo S5003INFOBASEPERANTE'), ('can_see_menu_s5003infoBasePerAntE', 'Pode visualizar no menu o modelo S5003INFOBASEPERANTE'), ('can_print_list_s5003infoBasePerAntE', 'Pode imprimir listagem do modelo S5003INFOBASEPERANTE'), ('can_print_data_s5003infoBasePerAntE', 'Pode imprimir o conte\xfado do modelo S5003INFOBASEPERANTE'))},
        ),
        migrations.AlterModelOptions(
            name='s5003infodpsfgts',
            options={'managed': True, 'ordering': ['s5003_evtbasesfgts'], 'permissions': (('can_see_list_s5003infoDpsFGTS', 'Pode ver listagem do modelo S5003INFODPSFGTS'), ('can_see_data_s5003infoDpsFGTS', 'Pode visualizar o conte\xfado do modelo S5003INFODPSFGTS'), ('can_see_menu_s5003infoDpsFGTS', 'Pode visualizar no menu o modelo S5003INFODPSFGTS'), ('can_print_list_s5003infoDpsFGTS', 'Pode imprimir listagem do modelo S5003INFODPSFGTS'), ('can_print_data_s5003infoDpsFGTS', 'Pode imprimir o conte\xfado do modelo S5003INFODPSFGTS'))},
        ),
        migrations.AlterModelOptions(
            name='s5003infodpsperante',
            options={'managed': True, 'ordering': ['s5003_infotrabdps', 'perref'], 'permissions': (('can_see_list_s5003infoDpsPerAntE', 'Pode ver listagem do modelo S5003INFODPSPERANTE'), ('can_see_data_s5003infoDpsPerAntE', 'Pode visualizar o conte\xfado do modelo S5003INFODPSPERANTE'), ('can_see_menu_s5003infoDpsPerAntE', 'Pode visualizar no menu o modelo S5003INFODPSPERANTE'), ('can_print_list_s5003infoDpsPerAntE', 'Pode imprimir listagem do modelo S5003INFODPSPERANTE'), ('can_print_data_s5003infoDpsPerAntE', 'Pode imprimir o conte\xfado do modelo S5003INFODPSPERANTE'))},
        ),
        migrations.AlterModelOptions(
            name='s5003infotrabdps',
            options={'managed': True, 'ordering': ['s5003_infodpsfgts', 'codcateg'], 'permissions': (('can_see_list_s5003infoTrabDps', 'Pode ver listagem do modelo S5003INFOTRABDPS'), ('can_see_data_s5003infoTrabDps', 'Pode visualizar o conte\xfado do modelo S5003INFOTRABDPS'), ('can_see_menu_s5003infoTrabDps', 'Pode visualizar no menu o modelo S5003INFOTRABDPS'), ('can_print_list_s5003infoTrabDps', 'Pode imprimir listagem do modelo S5003INFOTRABDPS'), ('can_print_data_s5003infoTrabDps', 'Pode imprimir o conte\xfado do modelo S5003INFOTRABDPS'))},
        ),
        migrations.AlterModelOptions(
            name='s5003infotrabfgts',
            options={'managed': True, 'ordering': ['s5003_ideestablot', 'codcateg'], 'permissions': (('can_see_list_s5003infoTrabFGTS', 'Pode ver listagem do modelo S5003INFOTRABFGTS'), ('can_see_data_s5003infoTrabFGTS', 'Pode visualizar o conte\xfado do modelo S5003INFOTRABFGTS'), ('can_see_menu_s5003infoTrabFGTS', 'Pode visualizar no menu o modelo S5003INFOTRABFGTS'), ('can_print_list_s5003infoTrabFGTS', 'Pode imprimir listagem do modelo S5003INFOTRABFGTS'), ('can_print_data_s5003infoTrabFGTS', 'Pode imprimir o conte\xfado do modelo S5003INFOTRABFGTS'))},
        ),
    ]
