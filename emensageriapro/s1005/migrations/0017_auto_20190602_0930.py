# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1005', '0016_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s1005alteracao',
            options={'managed': True, 'ordering': ['s1005_evttabestab', 'tpinsc', 'nrinsc', 'inivalid', 'cnaeprep', 'aliqrat', 'regpt', 'contapr'], 'permissions': (('can_see_list_s1005alteracao', 'Pode ver listagem do modelo S1005ALTERACAO'), ('can_see_data_s1005alteracao', 'Pode visualizar o conte\xfado do modelo S1005ALTERACAO'), ('can_see_menu_s1005alteracao', 'Pode visualizar no menu o modelo S1005ALTERACAO'), ('can_print_list_s1005alteracao', 'Pode imprimir listagem do modelo S1005ALTERACAO'), ('can_print_data_s1005alteracao', 'Pode imprimir o conte\xfado do modelo S1005ALTERACAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1005alteracaoinfocaepf',
            options={'managed': True, 'ordering': ['s1005_alteracao', 'tpcaepf'], 'permissions': (('can_see_list_s1005alteracaoinfoCaepf', 'Pode ver listagem do modelo S1005ALTERACAOINFOCAEPF'), ('can_see_data_s1005alteracaoinfoCaepf', 'Pode visualizar o conte\xfado do modelo S1005ALTERACAOINFOCAEPF'), ('can_see_menu_s1005alteracaoinfoCaepf', 'Pode visualizar no menu o modelo S1005ALTERACAOINFOCAEPF'), ('can_print_list_s1005alteracaoinfoCaepf', 'Pode imprimir listagem do modelo S1005ALTERACAOINFOCAEPF'), ('can_print_data_s1005alteracaoinfoCaepf', 'Pode imprimir o conte\xfado do modelo S1005ALTERACAOINFOCAEPF'))},
        ),
        migrations.AlterModelOptions(
            name='s1005alteracaoinfoenteduc',
            options={'managed': True, 'ordering': ['s1005_alteracao', 'nrinsc'], 'permissions': (('can_see_list_s1005alteracaoinfoEntEduc', 'Pode ver listagem do modelo S1005ALTERACAOINFOENTEDUC'), ('can_see_data_s1005alteracaoinfoEntEduc', 'Pode visualizar o conte\xfado do modelo S1005ALTERACAOINFOENTEDUC'), ('can_see_menu_s1005alteracaoinfoEntEduc', 'Pode visualizar no menu o modelo S1005ALTERACAOINFOENTEDUC'), ('can_print_list_s1005alteracaoinfoEntEduc', 'Pode imprimir listagem do modelo S1005ALTERACAOINFOENTEDUC'), ('can_print_data_s1005alteracaoinfoEntEduc', 'Pode imprimir o conte\xfado do modelo S1005ALTERACAOINFOENTEDUC'))},
        ),
        migrations.AlterModelOptions(
            name='s1005alteracaoinfoobra',
            options={'managed': True, 'ordering': ['s1005_alteracao', 'indsubstpatrobra'], 'permissions': (('can_see_list_s1005alteracaoinfoObra', 'Pode ver listagem do modelo S1005ALTERACAOINFOOBRA'), ('can_see_data_s1005alteracaoinfoObra', 'Pode visualizar o conte\xfado do modelo S1005ALTERACAOINFOOBRA'), ('can_see_menu_s1005alteracaoinfoObra', 'Pode visualizar no menu o modelo S1005ALTERACAOINFOOBRA'), ('can_print_list_s1005alteracaoinfoObra', 'Pode imprimir listagem do modelo S1005ALTERACAOINFOOBRA'), ('can_print_data_s1005alteracaoinfoObra', 'Pode imprimir o conte\xfado do modelo S1005ALTERACAOINFOOBRA'))},
        ),
        migrations.AlterModelOptions(
            name='s1005alteracaoinfopcd',
            options={'managed': True, 'ordering': ['s1005_alteracao', 'contpcd'], 'permissions': (('can_see_list_s1005alteracaoinfoPCD', 'Pode ver listagem do modelo S1005ALTERACAOINFOPCD'), ('can_see_data_s1005alteracaoinfoPCD', 'Pode visualizar o conte\xfado do modelo S1005ALTERACAOINFOPCD'), ('can_see_menu_s1005alteracaoinfoPCD', 'Pode visualizar no menu o modelo S1005ALTERACAOINFOPCD'), ('can_print_list_s1005alteracaoinfoPCD', 'Pode imprimir listagem do modelo S1005ALTERACAOINFOPCD'), ('can_print_data_s1005alteracaoinfoPCD', 'Pode imprimir o conte\xfado do modelo S1005ALTERACAOINFOPCD'))},
        ),
        migrations.AlterModelOptions(
            name='s1005alteracaonovavalidade',
            options={'managed': True, 'ordering': ['s1005_alteracao', 'inivalid'], 'permissions': (('can_see_list_s1005alteracaonovaValidade', 'Pode ver listagem do modelo S1005ALTERACAONOVAVALIDADE'), ('can_see_data_s1005alteracaonovaValidade', 'Pode visualizar o conte\xfado do modelo S1005ALTERACAONOVAVALIDADE'), ('can_see_menu_s1005alteracaonovaValidade', 'Pode visualizar no menu o modelo S1005ALTERACAONOVAVALIDADE'), ('can_print_list_s1005alteracaonovaValidade', 'Pode imprimir listagem do modelo S1005ALTERACAONOVAVALIDADE'), ('can_print_data_s1005alteracaonovaValidade', 'Pode imprimir o conte\xfado do modelo S1005ALTERACAONOVAVALIDADE'))},
        ),
        migrations.AlterModelOptions(
            name='s1005alteracaoprocadmjudfap',
            options={'managed': True, 'ordering': ['s1005_alteracao', 'tpproc', 'nrproc', 'codsusp'], 'permissions': (('can_see_list_s1005alteracaoprocAdmJudFap', 'Pode ver listagem do modelo S1005ALTERACAOPROCADMJUDFAP'), ('can_see_data_s1005alteracaoprocAdmJudFap', 'Pode visualizar o conte\xfado do modelo S1005ALTERACAOPROCADMJUDFAP'), ('can_see_menu_s1005alteracaoprocAdmJudFap', 'Pode visualizar no menu o modelo S1005ALTERACAOPROCADMJUDFAP'), ('can_print_list_s1005alteracaoprocAdmJudFap', 'Pode imprimir listagem do modelo S1005ALTERACAOPROCADMJUDFAP'), ('can_print_data_s1005alteracaoprocAdmJudFap', 'Pode imprimir o conte\xfado do modelo S1005ALTERACAOPROCADMJUDFAP'))},
        ),
        migrations.AlterModelOptions(
            name='s1005alteracaoprocadmjudrat',
            options={'managed': True, 'ordering': ['s1005_alteracao', 'tpproc', 'nrproc', 'codsusp'], 'permissions': (('can_see_list_s1005alteracaoprocAdmJudRat', 'Pode ver listagem do modelo S1005ALTERACAOPROCADMJUDRAT'), ('can_see_data_s1005alteracaoprocAdmJudRat', 'Pode visualizar o conte\xfado do modelo S1005ALTERACAOPROCADMJUDRAT'), ('can_see_menu_s1005alteracaoprocAdmJudRat', 'Pode visualizar no menu o modelo S1005ALTERACAOPROCADMJUDRAT'), ('can_print_list_s1005alteracaoprocAdmJudRat', 'Pode imprimir listagem do modelo S1005ALTERACAOPROCADMJUDRAT'), ('can_print_data_s1005alteracaoprocAdmJudRat', 'Pode imprimir o conte\xfado do modelo S1005ALTERACAOPROCADMJUDRAT'))},
        ),
        migrations.AlterModelOptions(
            name='s1005exclusao',
            options={'managed': True, 'ordering': ['s1005_evttabestab', 'tpinsc', 'nrinsc', 'inivalid'], 'permissions': (('can_see_list_s1005exclusao', 'Pode ver listagem do modelo S1005EXCLUSAO'), ('can_see_data_s1005exclusao', 'Pode visualizar o conte\xfado do modelo S1005EXCLUSAO'), ('can_see_menu_s1005exclusao', 'Pode visualizar no menu o modelo S1005EXCLUSAO'), ('can_print_list_s1005exclusao', 'Pode imprimir listagem do modelo S1005EXCLUSAO'), ('can_print_data_s1005exclusao', 'Pode imprimir o conte\xfado do modelo S1005EXCLUSAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1005inclusao',
            options={'managed': True, 'ordering': ['s1005_evttabestab', 'tpinsc', 'nrinsc', 'inivalid', 'cnaeprep', 'aliqrat', 'regpt', 'contapr'], 'permissions': (('can_see_list_s1005inclusao', 'Pode ver listagem do modelo S1005INCLUSAO'), ('can_see_data_s1005inclusao', 'Pode visualizar o conte\xfado do modelo S1005INCLUSAO'), ('can_see_menu_s1005inclusao', 'Pode visualizar no menu o modelo S1005INCLUSAO'), ('can_print_list_s1005inclusao', 'Pode imprimir listagem do modelo S1005INCLUSAO'), ('can_print_data_s1005inclusao', 'Pode imprimir o conte\xfado do modelo S1005INCLUSAO'))},
        ),
        migrations.AlterModelOptions(
            name='s1005inclusaoinfocaepf',
            options={'managed': True, 'ordering': ['s1005_inclusao', 'tpcaepf'], 'permissions': (('can_see_list_s1005inclusaoinfoCaepf', 'Pode ver listagem do modelo S1005INCLUSAOINFOCAEPF'), ('can_see_data_s1005inclusaoinfoCaepf', 'Pode visualizar o conte\xfado do modelo S1005INCLUSAOINFOCAEPF'), ('can_see_menu_s1005inclusaoinfoCaepf', 'Pode visualizar no menu o modelo S1005INCLUSAOINFOCAEPF'), ('can_print_list_s1005inclusaoinfoCaepf', 'Pode imprimir listagem do modelo S1005INCLUSAOINFOCAEPF'), ('can_print_data_s1005inclusaoinfoCaepf', 'Pode imprimir o conte\xfado do modelo S1005INCLUSAOINFOCAEPF'))},
        ),
        migrations.AlterModelOptions(
            name='s1005inclusaoinfoenteduc',
            options={'managed': True, 'ordering': ['s1005_inclusao', 'nrinsc'], 'permissions': (('can_see_list_s1005inclusaoinfoEntEduc', 'Pode ver listagem do modelo S1005INCLUSAOINFOENTEDUC'), ('can_see_data_s1005inclusaoinfoEntEduc', 'Pode visualizar o conte\xfado do modelo S1005INCLUSAOINFOENTEDUC'), ('can_see_menu_s1005inclusaoinfoEntEduc', 'Pode visualizar no menu o modelo S1005INCLUSAOINFOENTEDUC'), ('can_print_list_s1005inclusaoinfoEntEduc', 'Pode imprimir listagem do modelo S1005INCLUSAOINFOENTEDUC'), ('can_print_data_s1005inclusaoinfoEntEduc', 'Pode imprimir o conte\xfado do modelo S1005INCLUSAOINFOENTEDUC'))},
        ),
        migrations.AlterModelOptions(
            name='s1005inclusaoinfoobra',
            options={'managed': True, 'ordering': ['s1005_inclusao', 'indsubstpatrobra'], 'permissions': (('can_see_list_s1005inclusaoinfoObra', 'Pode ver listagem do modelo S1005INCLUSAOINFOOBRA'), ('can_see_data_s1005inclusaoinfoObra', 'Pode visualizar o conte\xfado do modelo S1005INCLUSAOINFOOBRA'), ('can_see_menu_s1005inclusaoinfoObra', 'Pode visualizar no menu o modelo S1005INCLUSAOINFOOBRA'), ('can_print_list_s1005inclusaoinfoObra', 'Pode imprimir listagem do modelo S1005INCLUSAOINFOOBRA'), ('can_print_data_s1005inclusaoinfoObra', 'Pode imprimir o conte\xfado do modelo S1005INCLUSAOINFOOBRA'))},
        ),
        migrations.AlterModelOptions(
            name='s1005inclusaoinfopcd',
            options={'managed': True, 'ordering': ['s1005_inclusao', 'contpcd'], 'permissions': (('can_see_list_s1005inclusaoinfoPCD', 'Pode ver listagem do modelo S1005INCLUSAOINFOPCD'), ('can_see_data_s1005inclusaoinfoPCD', 'Pode visualizar o conte\xfado do modelo S1005INCLUSAOINFOPCD'), ('can_see_menu_s1005inclusaoinfoPCD', 'Pode visualizar no menu o modelo S1005INCLUSAOINFOPCD'), ('can_print_list_s1005inclusaoinfoPCD', 'Pode imprimir listagem do modelo S1005INCLUSAOINFOPCD'), ('can_print_data_s1005inclusaoinfoPCD', 'Pode imprimir o conte\xfado do modelo S1005INCLUSAOINFOPCD'))},
        ),
        migrations.AlterModelOptions(
            name='s1005inclusaoprocadmjudfap',
            options={'managed': True, 'ordering': ['s1005_inclusao', 'tpproc', 'nrproc', 'codsusp'], 'permissions': (('can_see_list_s1005inclusaoprocAdmJudFap', 'Pode ver listagem do modelo S1005INCLUSAOPROCADMJUDFAP'), ('can_see_data_s1005inclusaoprocAdmJudFap', 'Pode visualizar o conte\xfado do modelo S1005INCLUSAOPROCADMJUDFAP'), ('can_see_menu_s1005inclusaoprocAdmJudFap', 'Pode visualizar no menu o modelo S1005INCLUSAOPROCADMJUDFAP'), ('can_print_list_s1005inclusaoprocAdmJudFap', 'Pode imprimir listagem do modelo S1005INCLUSAOPROCADMJUDFAP'), ('can_print_data_s1005inclusaoprocAdmJudFap', 'Pode imprimir o conte\xfado do modelo S1005INCLUSAOPROCADMJUDFAP'))},
        ),
        migrations.AlterModelOptions(
            name='s1005inclusaoprocadmjudrat',
            options={'managed': True, 'ordering': ['s1005_inclusao', 'tpproc', 'nrproc', 'codsusp'], 'permissions': (('can_see_list_s1005inclusaoprocAdmJudRat', 'Pode ver listagem do modelo S1005INCLUSAOPROCADMJUDRAT'), ('can_see_data_s1005inclusaoprocAdmJudRat', 'Pode visualizar o conte\xfado do modelo S1005INCLUSAOPROCADMJUDRAT'), ('can_see_menu_s1005inclusaoprocAdmJudRat', 'Pode visualizar no menu o modelo S1005INCLUSAOPROCADMJUDRAT'), ('can_print_list_s1005inclusaoprocAdmJudRat', 'Pode imprimir listagem do modelo S1005INCLUSAOPROCADMJUDRAT'), ('can_print_data_s1005inclusaoprocAdmJudRat', 'Pode imprimir o conte\xfado do modelo S1005INCLUSAOPROCADMJUDRAT'))},
        ),
    ]
