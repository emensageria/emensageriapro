# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2299', '0016_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2299dmdev',
            options={'managed': True, 'ordering': ['s2299_verbasresc', 'idedmdev'], 'permissions': (('can_see_list_s2299dmDev', 'Pode ver listagem do modelo S2299DMDEV'), ('can_see_data_s2299dmDev', 'Pode visualizar o conte\xfado do modelo S2299DMDEV'), ('can_see_menu_s2299dmDev', 'Pode visualizar no menu o modelo S2299DMDEV'), ('can_print_list_s2299dmDev', 'Pode imprimir listagem do modelo S2299DMDEV'), ('can_print_data_s2299dmDev', 'Pode imprimir o conte\xfado do modelo S2299DMDEV'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperant',
            options={'managed': True, 'ordering': ['s2299_dmdev'], 'permissions': (('can_see_list_s2299infoPerAnt', 'Pode ver listagem do modelo S2299INFOPERANT'), ('can_see_data_s2299infoPerAnt', 'Pode visualizar o conte\xfado do modelo S2299INFOPERANT'), ('can_see_menu_s2299infoPerAnt', 'Pode visualizar no menu o modelo S2299INFOPERANT'), ('can_print_list_s2299infoPerAnt', 'Pode imprimir listagem do modelo S2299INFOPERANT'), ('can_print_data_s2299infoPerAnt', 'Pode imprimir o conte\xfado do modelo S2299INFOPERANT'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperantdetverbas',
            options={'managed': True, 'ordering': ['s2299_infoperant_ideestablot', 'codrubr', 'idetabrubr', 'vrrubr'], 'permissions': (('can_see_list_s2299infoPerAntdetVerbas', 'Pode ver listagem do modelo S2299INFOPERANTDETVERBAS'), ('can_see_data_s2299infoPerAntdetVerbas', 'Pode visualizar o conte\xfado do modelo S2299INFOPERANTDETVERBAS'), ('can_see_menu_s2299infoPerAntdetVerbas', 'Pode visualizar no menu o modelo S2299INFOPERANTDETVERBAS'), ('can_print_list_s2299infoPerAntdetVerbas', 'Pode imprimir listagem do modelo S2299INFOPERANTDETVERBAS'), ('can_print_data_s2299infoPerAntdetVerbas', 'Pode imprimir o conte\xfado do modelo S2299INFOPERANTDETVERBAS'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperantideadc',
            options={'managed': True, 'ordering': ['s2299_infoperant', 'dtacconv', 'tpacconv', 'dtefacconv', 'dsc'], 'permissions': (('can_see_list_s2299infoPerAntideADC', 'Pode ver listagem do modelo S2299INFOPERANTIDEADC'), ('can_see_data_s2299infoPerAntideADC', 'Pode visualizar o conte\xfado do modelo S2299INFOPERANTIDEADC'), ('can_see_menu_s2299infoPerAntideADC', 'Pode visualizar no menu o modelo S2299INFOPERANTIDEADC'), ('can_print_list_s2299infoPerAntideADC', 'Pode imprimir listagem do modelo S2299INFOPERANTIDEADC'), ('can_print_data_s2299infoPerAntideADC', 'Pode imprimir o conte\xfado do modelo S2299INFOPERANTIDEADC'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperantideestablot',
            options={'managed': True, 'ordering': ['s2299_infoperant_ideperiodo', 'tpinsc', 'nrinsc', 'codlotacao'], 'permissions': (('can_see_list_s2299infoPerAntideEstabLot', 'Pode ver listagem do modelo S2299INFOPERANTIDEESTABLOT'), ('can_see_data_s2299infoPerAntideEstabLot', 'Pode visualizar o conte\xfado do modelo S2299INFOPERANTIDEESTABLOT'), ('can_see_menu_s2299infoPerAntideEstabLot', 'Pode visualizar no menu o modelo S2299INFOPERANTIDEESTABLOT'), ('can_print_list_s2299infoPerAntideEstabLot', 'Pode imprimir listagem do modelo S2299INFOPERANTIDEESTABLOT'), ('can_print_data_s2299infoPerAntideEstabLot', 'Pode imprimir o conte\xfado do modelo S2299INFOPERANTIDEESTABLOT'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperantideperiodo',
            options={'managed': True, 'ordering': ['s2299_infoperant_ideadc', 'perref'], 'permissions': (('can_see_list_s2299infoPerAntidePeriodo', 'Pode ver listagem do modelo S2299INFOPERANTIDEPERIODO'), ('can_see_data_s2299infoPerAntidePeriodo', 'Pode visualizar o conte\xfado do modelo S2299INFOPERANTIDEPERIODO'), ('can_see_menu_s2299infoPerAntidePeriodo', 'Pode visualizar no menu o modelo S2299INFOPERANTIDEPERIODO'), ('can_print_list_s2299infoPerAntidePeriodo', 'Pode imprimir listagem do modelo S2299INFOPERANTIDEPERIODO'), ('can_print_data_s2299infoPerAntidePeriodo', 'Pode imprimir o conte\xfado do modelo S2299INFOPERANTIDEPERIODO'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperantinfoagnocivo',
            options={'managed': True, 'ordering': ['s2299_infoperant_ideestablot', 'grauexp'], 'permissions': (('can_see_list_s2299infoPerAntinfoAgNocivo', 'Pode ver listagem do modelo S2299INFOPERANTINFOAGNOCIVO'), ('can_see_data_s2299infoPerAntinfoAgNocivo', 'Pode visualizar o conte\xfado do modelo S2299INFOPERANTINFOAGNOCIVO'), ('can_see_menu_s2299infoPerAntinfoAgNocivo', 'Pode visualizar no menu o modelo S2299INFOPERANTINFOAGNOCIVO'), ('can_print_list_s2299infoPerAntinfoAgNocivo', 'Pode imprimir listagem do modelo S2299INFOPERANTINFOAGNOCIVO'), ('can_print_data_s2299infoPerAntinfoAgNocivo', 'Pode imprimir o conte\xfado do modelo S2299INFOPERANTINFOAGNOCIVO'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperantinfosimples',
            options={'managed': True, 'ordering': ['s2299_infoperant_ideestablot', 'indsimples'], 'permissions': (('can_see_list_s2299infoPerAntinfoSimples', 'Pode ver listagem do modelo S2299INFOPERANTINFOSIMPLES'), ('can_see_data_s2299infoPerAntinfoSimples', 'Pode visualizar o conte\xfado do modelo S2299INFOPERANTINFOSIMPLES'), ('can_see_menu_s2299infoPerAntinfoSimples', 'Pode visualizar no menu o modelo S2299INFOPERANTINFOSIMPLES'), ('can_print_list_s2299infoPerAntinfoSimples', 'Pode imprimir listagem do modelo S2299INFOPERANTINFOSIMPLES'), ('can_print_data_s2299infoPerAntinfoSimples', 'Pode imprimir o conte\xfado do modelo S2299INFOPERANTINFOSIMPLES'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperapur',
            options={'managed': True, 'ordering': ['s2299_dmdev'], 'permissions': (('can_see_list_s2299infoPerApur', 'Pode ver listagem do modelo S2299INFOPERAPUR'), ('can_see_data_s2299infoPerApur', 'Pode visualizar o conte\xfado do modelo S2299INFOPERAPUR'), ('can_see_menu_s2299infoPerApur', 'Pode visualizar no menu o modelo S2299INFOPERAPUR'), ('can_print_list_s2299infoPerApur', 'Pode imprimir listagem do modelo S2299INFOPERAPUR'), ('can_print_data_s2299infoPerApur', 'Pode imprimir o conte\xfado do modelo S2299INFOPERAPUR'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperapurdetoper',
            options={'managed': True, 'ordering': ['s2299_infoperapur_infosaudecolet', 'cnpjoper', 'regans', 'vrpgtit'], 'permissions': (('can_see_list_s2299infoPerApurdetOper', 'Pode ver listagem do modelo S2299INFOPERAPURDETOPER'), ('can_see_data_s2299infoPerApurdetOper', 'Pode visualizar o conte\xfado do modelo S2299INFOPERAPURDETOPER'), ('can_see_menu_s2299infoPerApurdetOper', 'Pode visualizar no menu o modelo S2299INFOPERAPURDETOPER'), ('can_print_list_s2299infoPerApurdetOper', 'Pode imprimir listagem do modelo S2299INFOPERAPURDETOPER'), ('can_print_data_s2299infoPerApurdetOper', 'Pode imprimir o conte\xfado do modelo S2299INFOPERAPURDETOPER'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperapurdetplano',
            options={'managed': True, 'ordering': ['s2299_infoperapur_detoper', 'tpdep', 'nmdep', 'dtnascto', 'vlrpgdep'], 'permissions': (('can_see_list_s2299infoPerApurdetPlano', 'Pode ver listagem do modelo S2299INFOPERAPURDETPLANO'), ('can_see_data_s2299infoPerApurdetPlano', 'Pode visualizar o conte\xfado do modelo S2299INFOPERAPURDETPLANO'), ('can_see_menu_s2299infoPerApurdetPlano', 'Pode visualizar no menu o modelo S2299INFOPERAPURDETPLANO'), ('can_print_list_s2299infoPerApurdetPlano', 'Pode imprimir listagem do modelo S2299INFOPERAPURDETPLANO'), ('can_print_data_s2299infoPerApurdetPlano', 'Pode imprimir o conte\xfado do modelo S2299INFOPERAPURDETPLANO'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperapurdetverbas',
            options={'managed': True, 'ordering': ['s2299_infoperapur_ideestablot', 'codrubr', 'idetabrubr', 'vrrubr'], 'permissions': (('can_see_list_s2299infoPerApurdetVerbas', 'Pode ver listagem do modelo S2299INFOPERAPURDETVERBAS'), ('can_see_data_s2299infoPerApurdetVerbas', 'Pode visualizar o conte\xfado do modelo S2299INFOPERAPURDETVERBAS'), ('can_see_menu_s2299infoPerApurdetVerbas', 'Pode visualizar no menu o modelo S2299INFOPERAPURDETVERBAS'), ('can_print_list_s2299infoPerApurdetVerbas', 'Pode imprimir listagem do modelo S2299INFOPERAPURDETVERBAS'), ('can_print_data_s2299infoPerApurdetVerbas', 'Pode imprimir o conte\xfado do modelo S2299INFOPERAPURDETVERBAS'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperapurideestablot',
            options={'managed': True, 'ordering': ['s2299_infoperapur', 'tpinsc', 'nrinsc', 'codlotacao'], 'permissions': (('can_see_list_s2299infoPerApurideEstabLot', 'Pode ver listagem do modelo S2299INFOPERAPURIDEESTABLOT'), ('can_see_data_s2299infoPerApurideEstabLot', 'Pode visualizar o conte\xfado do modelo S2299INFOPERAPURIDEESTABLOT'), ('can_see_menu_s2299infoPerApurideEstabLot', 'Pode visualizar no menu o modelo S2299INFOPERAPURIDEESTABLOT'), ('can_print_list_s2299infoPerApurideEstabLot', 'Pode imprimir listagem do modelo S2299INFOPERAPURIDEESTABLOT'), ('can_print_data_s2299infoPerApurideEstabLot', 'Pode imprimir o conte\xfado do modelo S2299INFOPERAPURIDEESTABLOT'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperapurinfoagnocivo',
            options={'managed': True, 'ordering': ['s2299_infoperapur_ideestablot', 'grauexp'], 'permissions': (('can_see_list_s2299infoPerApurinfoAgNocivo', 'Pode ver listagem do modelo S2299INFOPERAPURINFOAGNOCIVO'), ('can_see_data_s2299infoPerApurinfoAgNocivo', 'Pode visualizar o conte\xfado do modelo S2299INFOPERAPURINFOAGNOCIVO'), ('can_see_menu_s2299infoPerApurinfoAgNocivo', 'Pode visualizar no menu o modelo S2299INFOPERAPURINFOAGNOCIVO'), ('can_print_list_s2299infoPerApurinfoAgNocivo', 'Pode imprimir listagem do modelo S2299INFOPERAPURINFOAGNOCIVO'), ('can_print_data_s2299infoPerApurinfoAgNocivo', 'Pode imprimir o conte\xfado do modelo S2299INFOPERAPURINFOAGNOCIVO'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperapurinfosaudecolet',
            options={'managed': True, 'ordering': ['s2299_infoperapur_ideestablot'], 'permissions': (('can_see_list_s2299infoPerApurinfoSaudeColet', 'Pode ver listagem do modelo S2299INFOPERAPURINFOSAUDECOLET'), ('can_see_data_s2299infoPerApurinfoSaudeColet', 'Pode visualizar o conte\xfado do modelo S2299INFOPERAPURINFOSAUDECOLET'), ('can_see_menu_s2299infoPerApurinfoSaudeColet', 'Pode visualizar no menu o modelo S2299INFOPERAPURINFOSAUDECOLET'), ('can_print_list_s2299infoPerApurinfoSaudeColet', 'Pode imprimir listagem do modelo S2299INFOPERAPURINFOSAUDECOLET'), ('can_print_data_s2299infoPerApurinfoSaudeColet', 'Pode imprimir o conte\xfado do modelo S2299INFOPERAPURINFOSAUDECOLET'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infoperapurinfosimples',
            options={'managed': True, 'ordering': ['s2299_infoperapur_ideestablot', 'indsimples'], 'permissions': (('can_see_list_s2299infoPerApurinfoSimples', 'Pode ver listagem do modelo S2299INFOPERAPURINFOSIMPLES'), ('can_see_data_s2299infoPerApurinfoSimples', 'Pode visualizar o conte\xfado do modelo S2299INFOPERAPURINFOSIMPLES'), ('can_see_menu_s2299infoPerApurinfoSimples', 'Pode visualizar no menu o modelo S2299INFOPERAPURINFOSIMPLES'), ('can_print_list_s2299infoPerApurinfoSimples', 'Pode imprimir listagem do modelo S2299INFOPERAPURINFOSIMPLES'), ('can_print_data_s2299infoPerApurinfoSimples', 'Pode imprimir o conte\xfado do modelo S2299INFOPERAPURINFOSIMPLES'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infotrabinterm',
            options={'managed': True, 'ordering': ['s2299_dmdev', 'codconv'], 'permissions': (('can_see_list_s2299infoTrabInterm', 'Pode ver listagem do modelo S2299INFOTRABINTERM'), ('can_see_data_s2299infoTrabInterm', 'Pode visualizar o conte\xfado do modelo S2299INFOTRABINTERM'), ('can_see_menu_s2299infoTrabInterm', 'Pode visualizar no menu o modelo S2299INFOTRABINTERM'), ('can_print_list_s2299infoTrabInterm', 'Pode imprimir listagem do modelo S2299INFOTRABINTERM'), ('can_print_data_s2299infoTrabInterm', 'Pode imprimir o conte\xfado do modelo S2299INFOTRABINTERM'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infotrabintermconsigfgts',
            options={'managed': True, 'ordering': ['s2299_evtdeslig', 'insconsig', 'nrcontr'], 'permissions': (('can_see_list_s2299infoTrabIntermconsigFGTS', 'Pode ver listagem do modelo S2299INFOTRABINTERMCONSIGFGTS'), ('can_see_data_s2299infoTrabIntermconsigFGTS', 'Pode visualizar o conte\xfado do modelo S2299INFOTRABINTERMCONSIGFGTS'), ('can_see_menu_s2299infoTrabIntermconsigFGTS', 'Pode visualizar no menu o modelo S2299INFOTRABINTERMCONSIGFGTS'), ('can_print_list_s2299infoTrabIntermconsigFGTS', 'Pode imprimir listagem do modelo S2299INFOTRABINTERMCONSIGFGTS'), ('can_print_data_s2299infoTrabIntermconsigFGTS', 'Pode imprimir o conte\xfado do modelo S2299INFOTRABINTERMCONSIGFGTS'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infotrabinterminfomv',
            options={'managed': True, 'ordering': ['s2299_verbasresc', 'indmv'], 'permissions': (('can_see_list_s2299infoTrabInterminfoMV', 'Pode ver listagem do modelo S2299INFOTRABINTERMINFOMV'), ('can_see_data_s2299infoTrabInterminfoMV', 'Pode visualizar o conte\xfado do modelo S2299INFOTRABINTERMINFOMV'), ('can_see_menu_s2299infoTrabInterminfoMV', 'Pode visualizar no menu o modelo S2299INFOTRABINTERMINFOMV'), ('can_print_list_s2299infoTrabInterminfoMV', 'Pode imprimir listagem do modelo S2299INFOTRABINTERMINFOMV'), ('can_print_data_s2299infoTrabInterminfoMV', 'Pode imprimir o conte\xfado do modelo S2299INFOTRABINTERMINFOMV'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infotrabintermproccs',
            options={'managed': True, 'ordering': ['s2299_verbasresc', 'nrprocjud'], 'permissions': (('can_see_list_s2299infoTrabIntermprocCS', 'Pode ver listagem do modelo S2299INFOTRABINTERMPROCCS'), ('can_see_data_s2299infoTrabIntermprocCS', 'Pode visualizar o conte\xfado do modelo S2299INFOTRABINTERMPROCCS'), ('can_see_menu_s2299infoTrabIntermprocCS', 'Pode visualizar no menu o modelo S2299INFOTRABINTERMPROCCS'), ('can_print_list_s2299infoTrabIntermprocCS', 'Pode imprimir listagem do modelo S2299INFOTRABINTERMPROCCS'), ('can_print_data_s2299infoTrabIntermprocCS', 'Pode imprimir o conte\xfado do modelo S2299INFOTRABINTERMPROCCS'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infotrabintermprocjudtrab',
            options={'managed': True, 'ordering': ['s2299_verbasresc', 'tptrib', 'nrprocjud'], 'permissions': (('can_see_list_s2299infoTrabIntermprocJudTrab', 'Pode ver listagem do modelo S2299INFOTRABINTERMPROCJUDTRAB'), ('can_see_data_s2299infoTrabIntermprocJudTrab', 'Pode visualizar o conte\xfado do modelo S2299INFOTRABINTERMPROCJUDTRAB'), ('can_see_menu_s2299infoTrabIntermprocJudTrab', 'Pode visualizar no menu o modelo S2299INFOTRABINTERMPROCJUDTRAB'), ('can_print_list_s2299infoTrabIntermprocJudTrab', 'Pode imprimir listagem do modelo S2299INFOTRABINTERMPROCJUDTRAB'), ('can_print_data_s2299infoTrabIntermprocJudTrab', 'Pode imprimir o conte\xfado do modelo S2299INFOTRABINTERMPROCJUDTRAB'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infotrabintermquarentena',
            options={'managed': True, 'ordering': ['s2299_evtdeslig', 'dtfimquar'], 'permissions': (('can_see_list_s2299infoTrabIntermquarentena', 'Pode ver listagem do modelo S2299INFOTRABINTERMQUARENTENA'), ('can_see_data_s2299infoTrabIntermquarentena', 'Pode visualizar o conte\xfado do modelo S2299INFOTRABINTERMQUARENTENA'), ('can_see_menu_s2299infoTrabIntermquarentena', 'Pode visualizar no menu o modelo S2299INFOTRABINTERMQUARENTENA'), ('can_print_list_s2299infoTrabIntermquarentena', 'Pode imprimir listagem do modelo S2299INFOTRABINTERMQUARENTENA'), ('can_print_data_s2299infoTrabIntermquarentena', 'Pode imprimir o conte\xfado do modelo S2299INFOTRABINTERMQUARENTENA'))},
        ),
        migrations.AlterModelOptions(
            name='s2299infotrabintermremunoutrempr',
            options={'managed': True, 'ordering': ['s2299_infotrabinterm_infomv', 'tpinsc', 'nrinsc', 'codcateg', 'vlrremunoe'], 'permissions': (('can_see_list_s2299infoTrabIntermremunOutrEmpr', 'Pode ver listagem do modelo S2299INFOTRABINTERMREMUNOUTREMPR'), ('can_see_data_s2299infoTrabIntermremunOutrEmpr', 'Pode visualizar o conte\xfado do modelo S2299INFOTRABINTERMREMUNOUTREMPR'), ('can_see_menu_s2299infoTrabIntermremunOutrEmpr', 'Pode visualizar no menu o modelo S2299INFOTRABINTERMREMUNOUTREMPR'), ('can_print_list_s2299infoTrabIntermremunOutrEmpr', 'Pode imprimir listagem do modelo S2299INFOTRABINTERMREMUNOUTREMPR'), ('can_print_data_s2299infoTrabIntermremunOutrEmpr', 'Pode imprimir o conte\xfado do modelo S2299INFOTRABINTERMREMUNOUTREMPR'))},
        ),
        migrations.AlterModelOptions(
            name='s2299mudancacpf',
            options={'managed': True, 'ordering': ['s2299_evtdeslig', 'novocpf'], 'permissions': (('can_see_list_s2299mudancaCPF', 'Pode ver listagem do modelo S2299MUDANCACPF'), ('can_see_data_s2299mudancaCPF', 'Pode visualizar o conte\xfado do modelo S2299MUDANCACPF'), ('can_see_menu_s2299mudancaCPF', 'Pode visualizar no menu o modelo S2299MUDANCACPF'), ('can_print_list_s2299mudancaCPF', 'Pode imprimir listagem do modelo S2299MUDANCACPF'), ('can_print_data_s2299mudancaCPF', 'Pode imprimir o conte\xfado do modelo S2299MUDANCACPF'))},
        ),
        migrations.AlterModelOptions(
            name='s2299observacoes',
            options={'managed': True, 'ordering': ['s2299_evtdeslig', 'observacao'], 'permissions': (('can_see_list_s2299observacoes', 'Pode ver listagem do modelo S2299OBSERVACOES'), ('can_see_data_s2299observacoes', 'Pode visualizar o conte\xfado do modelo S2299OBSERVACOES'), ('can_see_menu_s2299observacoes', 'Pode visualizar no menu o modelo S2299OBSERVACOES'), ('can_print_list_s2299observacoes', 'Pode imprimir listagem do modelo S2299OBSERVACOES'), ('can_print_data_s2299observacoes', 'Pode imprimir o conte\xfado do modelo S2299OBSERVACOES'))},
        ),
        migrations.AlterModelOptions(
            name='s2299sucessaovinc',
            options={'managed': True, 'ordering': ['s2299_evtdeslig', 'tpinscsuc', 'cnpjsucessora'], 'permissions': (('can_see_list_s2299sucessaoVinc', 'Pode ver listagem do modelo S2299SUCESSAOVINC'), ('can_see_data_s2299sucessaoVinc', 'Pode visualizar o conte\xfado do modelo S2299SUCESSAOVINC'), ('can_see_menu_s2299sucessaoVinc', 'Pode visualizar no menu o modelo S2299SUCESSAOVINC'), ('can_print_list_s2299sucessaoVinc', 'Pode imprimir listagem do modelo S2299SUCESSAOVINC'), ('can_print_data_s2299sucessaoVinc', 'Pode imprimir o conte\xfado do modelo S2299SUCESSAOVINC'))},
        ),
        migrations.AlterModelOptions(
            name='s2299transftit',
            options={'managed': True, 'ordering': ['s2299_evtdeslig', 'cpfsubstituto', 'dtnascto'], 'permissions': (('can_see_list_s2299transfTit', 'Pode ver listagem do modelo S2299TRANSFTIT'), ('can_see_data_s2299transfTit', 'Pode visualizar o conte\xfado do modelo S2299TRANSFTIT'), ('can_see_menu_s2299transfTit', 'Pode visualizar no menu o modelo S2299TRANSFTIT'), ('can_print_list_s2299transfTit', 'Pode imprimir listagem do modelo S2299TRANSFTIT'), ('can_print_data_s2299transfTit', 'Pode imprimir o conte\xfado do modelo S2299TRANSFTIT'))},
        ),
        migrations.AlterModelOptions(
            name='s2299verbasresc',
            options={'managed': True, 'ordering': ['s2299_evtdeslig'], 'permissions': (('can_see_list_s2299verbasResc', 'Pode ver listagem do modelo S2299VERBASRESC'), ('can_see_data_s2299verbasResc', 'Pode visualizar o conte\xfado do modelo S2299VERBASRESC'), ('can_see_menu_s2299verbasResc', 'Pode visualizar no menu o modelo S2299VERBASRESC'), ('can_print_list_s2299verbasResc', 'Pode imprimir listagem do modelo S2299VERBASRESC'), ('can_print_data_s2299verbasResc', 'Pode imprimir o conte\xfado do modelo S2299VERBASRESC'))},
        ),
    ]
