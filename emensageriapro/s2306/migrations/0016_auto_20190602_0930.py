# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-02 09:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s2306', '0015_auto_20190531_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='s2306ageintegracao',
            options={'managed': True, 'ordering': ['s2306_infoestagiario', 'cnpjagntinteg', 'nmrazao', 'dsclograd', 'nrlograd', 'cep', 'uf'], 'permissions': (('can_see_list_s2306ageIntegracao', 'Pode ver listagem do modelo S2306AGEINTEGRACAO'), ('can_see_data_s2306ageIntegracao', 'Pode visualizar o conte\xfado do modelo S2306AGEINTEGRACAO'), ('can_see_menu_s2306ageIntegracao', 'Pode visualizar no menu o modelo S2306AGEINTEGRACAO'), ('can_print_list_s2306ageIntegracao', 'Pode imprimir listagem do modelo S2306AGEINTEGRACAO'), ('can_print_data_s2306ageIntegracao', 'Pode imprimir o conte\xfado do modelo S2306AGEINTEGRACAO'))},
        ),
        migrations.AlterModelOptions(
            name='s2306cargofuncao',
            options={'managed': True, 'ordering': ['s2306_infocomplementares', 'codcargo'], 'permissions': (('can_see_list_s2306cargoFuncao', 'Pode ver listagem do modelo S2306CARGOFUNCAO'), ('can_see_data_s2306cargoFuncao', 'Pode visualizar o conte\xfado do modelo S2306CARGOFUNCAO'), ('can_see_menu_s2306cargoFuncao', 'Pode visualizar no menu o modelo S2306CARGOFUNCAO'), ('can_print_list_s2306cargoFuncao', 'Pode imprimir listagem do modelo S2306CARGOFUNCAO'), ('can_print_data_s2306cargoFuncao', 'Pode imprimir o conte\xfado do modelo S2306CARGOFUNCAO'))},
        ),
        migrations.AlterModelOptions(
            name='s2306infocomplementares',
            options={'managed': True, 'ordering': ['s2306_evttsvaltcontr'], 'permissions': (('can_see_list_s2306infoComplementares', 'Pode ver listagem do modelo S2306INFOCOMPLEMENTARES'), ('can_see_data_s2306infoComplementares', 'Pode visualizar o conte\xfado do modelo S2306INFOCOMPLEMENTARES'), ('can_see_menu_s2306infoComplementares', 'Pode visualizar no menu o modelo S2306INFOCOMPLEMENTARES'), ('can_print_list_s2306infoComplementares', 'Pode imprimir listagem do modelo S2306INFOCOMPLEMENTARES'), ('can_print_data_s2306infoComplementares', 'Pode imprimir o conte\xfado do modelo S2306INFOCOMPLEMENTARES'))},
        ),
        migrations.AlterModelOptions(
            name='s2306infoestagiario',
            options={'managed': True, 'ordering': ['s2306_infocomplementares', 'natestagio', 'nivestagio', 'dtprevterm', 'nmrazao'], 'permissions': (('can_see_list_s2306infoEstagiario', 'Pode ver listagem do modelo S2306INFOESTAGIARIO'), ('can_see_data_s2306infoEstagiario', 'Pode visualizar o conte\xfado do modelo S2306INFOESTAGIARIO'), ('can_see_menu_s2306infoEstagiario', 'Pode visualizar no menu o modelo S2306INFOESTAGIARIO'), ('can_print_list_s2306infoEstagiario', 'Pode imprimir listagem do modelo S2306INFOESTAGIARIO'), ('can_print_data_s2306infoEstagiario', 'Pode imprimir o conte\xfado do modelo S2306INFOESTAGIARIO'))},
        ),
        migrations.AlterModelOptions(
            name='s2306infotrabcedido',
            options={'managed': True, 'ordering': ['s2306_infocomplementares', 'indremuncargo'], 'permissions': (('can_see_list_s2306infoTrabCedido', 'Pode ver listagem do modelo S2306INFOTRABCEDIDO'), ('can_see_data_s2306infoTrabCedido', 'Pode visualizar o conte\xfado do modelo S2306INFOTRABCEDIDO'), ('can_see_menu_s2306infoTrabCedido', 'Pode visualizar no menu o modelo S2306INFOTRABCEDIDO'), ('can_print_list_s2306infoTrabCedido', 'Pode imprimir listagem do modelo S2306INFOTRABCEDIDO'), ('can_print_data_s2306infoTrabCedido', 'Pode imprimir o conte\xfado do modelo S2306INFOTRABCEDIDO'))},
        ),
        migrations.AlterModelOptions(
            name='s2306remuneracao',
            options={'managed': True, 'ordering': ['s2306_infocomplementares', 'vrsalfx', 'undsalfixo'], 'permissions': (('can_see_list_s2306remuneracao', 'Pode ver listagem do modelo S2306REMUNERACAO'), ('can_see_data_s2306remuneracao', 'Pode visualizar o conte\xfado do modelo S2306REMUNERACAO'), ('can_see_menu_s2306remuneracao', 'Pode visualizar no menu o modelo S2306REMUNERACAO'), ('can_print_list_s2306remuneracao', 'Pode imprimir listagem do modelo S2306REMUNERACAO'), ('can_print_data_s2306remuneracao', 'Pode imprimir o conte\xfado do modelo S2306REMUNERACAO'))},
        ),
        migrations.AlterModelOptions(
            name='s2306supervisorestagio',
            options={'managed': True, 'ordering': ['s2306_infoestagiario', 'cpfsupervisor', 'nmsuperv'], 'permissions': (('can_see_list_s2306supervisorEstagio', 'Pode ver listagem do modelo S2306SUPERVISORESTAGIO'), ('can_see_data_s2306supervisorEstagio', 'Pode visualizar o conte\xfado do modelo S2306SUPERVISORESTAGIO'), ('can_see_menu_s2306supervisorEstagio', 'Pode visualizar no menu o modelo S2306SUPERVISORESTAGIO'), ('can_print_list_s2306supervisorEstagio', 'Pode imprimir listagem do modelo S2306SUPERVISORESTAGIO'), ('can_print_data_s2306supervisorEstagio', 'Pode imprimir o conte\xfado do modelo S2306SUPERVISORESTAGIO'))},
        ),
    ]
