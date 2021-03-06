# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0013_auto_20190202_1551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arquivos',
            options={'managed': True, 'permissions': (('can_view_arquivos', 'Can view arquivos'),)},
        ),
        migrations.AlterModelOptions(
            name='importacaoarquivos',
            options={'managed': True, 'ordering': ['arquivo'], 'permissions': (('can_view_importacao_arquivos', 'Can view importacao_arquivos'),)},
        ),
        migrations.AlterModelOptions(
            name='importacaoarquivoseventos',
            options={'managed': True, 'ordering': ['importacao_arquivos', 'arquivo', 'evento', 'versao', 'identidade_evento', 'identidade'], 'permissions': (('can_view_importacao_arquivos_eventos', 'Can view importacao_arquivos_eventos'),)},
        ),
        migrations.AlterModelOptions(
            name='regrasdevalidacao',
            options={'managed': True, 'permissions': (('can_view_regras_validacao', 'Can view regras_validacao'),)},
        ),
        migrations.AlterModelOptions(
            name='relatorios',
            options={'managed': True, 'permissions': (('can_view_relatorios', 'Can view relatorios'),)},
        ),
        migrations.AlterModelOptions(
            name='retornoseventos',
            options={'managed': True, 'ordering': ['transmissor_lote_esocial', 'identidade'], 'permissions': (('can_view_retornos_eventos', 'Can view retornos_eventos'),)},
        ),
        migrations.AlterModelOptions(
            name='retornoseventoshorarios',
            options={'managed': True, 'permissions': (('can_view_retornos_eventos_horarios', 'Can view retornos_eventos_horarios'),)},
        ),
        migrations.AlterModelOptions(
            name='retornoseventosintervalos',
            options={'managed': True, 'permissions': (('can_view_retornos_eventos_intervalos', 'Can view retornos_eventos_intervalos'),)},
        ),
        migrations.AlterModelOptions(
            name='retornoseventosocorrencias',
            options={'managed': True, 'permissions': (('can_view_retornos_eventos_ocorrencias', 'Can view retornos_eventos_ocorrencias'),)},
        ),
        migrations.AlterModelOptions(
            name='transmissorlote',
            options={'managed': True, 'permissions': (('can_view_transmissores', 'Can view transmissores'),)},
        ),
        migrations.AlterModelOptions(
            name='transmissorloteefdreinf',
            options={'managed': True, 'permissions': (('can_view_transmissor_lote_efdreinf', 'Can view transmissor_lote_efdreinf'),)},
        ),
        migrations.AlterModelOptions(
            name='transmissorloteefdreinfocorrencias',
            options={'managed': True, 'permissions': (('can_view_transmissor_lote_efdreinf_ocorrencias', 'Can view transmissor_lote_efdreinf_ocorrencias'),)},
        ),
        migrations.AlterModelOptions(
            name='transmissorloteesocial',
            options={'managed': True, 'permissions': (('can_view_transmissor_lote_esocial', 'Can view transmissor_lote_esocial'),)},
        ),
        migrations.AlterModelOptions(
            name='transmissorloteesocialocorrencias',
            options={'managed': True, 'permissions': (('can_view_transmissor_lote_esocial_ocorrencias', 'Can view transmissor_lote_esocial_ocorrencias'),)},
        ),
    ]
