# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-23 09:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabelas', '0010_auto_20181121_0825'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='efdreinfcodigosatividadesprodutosservicoscprb',
            options={'managed': True, 'ordering': ['codigo', 'grupo', 'ncm', 'cr', 'inicio_escrituracao', 'descricao', 'incidencia', 'aliquota']},
        ),
        migrations.AlterModelOptions(
            name='efdreinfpagamentoscodigos',
            options={'managed': True, 'ordering': ['beneficiario_pf', 'beneficiario_pj', 'codigo', 'grupo', 'descricao']},
        ),
        migrations.AlterModelOptions(
            name='efdreinfregraspagamentoscodigos',
            options={'managed': True, 'ordering': ['classificacao', 'tributacao_com_exigibilidade_suspensa', 'compensacao_imposto_por_decisao_judicial', 'rendimentos_isentos', 'deducoes', 'decimo_terceiro', 'codigo', 'descricao']},
        ),
    ]