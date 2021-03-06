# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabelas', '0014_auto_20190202_1539'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cbo',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_cbo', 'Can view cbo'),)},
        ),
        migrations.AlterModelOptions(
            name='cid',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_cid', 'Can view cid'),)},
        ),
        migrations.AlterModelOptions(
            name='cnae',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_cnae', 'Can view cnae'),)},
        ),
        migrations.AlterModelOptions(
            name='efdreinfclassificacaoservicosprestados',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_efdreinf_classificacao_servicos_prestados', 'Can view efdreinf_classificacao_servicos_prestados'),)},
        ),
        migrations.AlterModelOptions(
            name='efdreinfclassificacaotributaria',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_efdreinf_classificacao_tributaria', 'Can view efdreinf_classificacao_tributaria'),)},
        ),
        migrations.AlterModelOptions(
            name='efdreinfcodigosatividadesprodutosservicoscprb',
            options={'managed': True, 'ordering': ['grupo', 'codigo', 'descricao', 'incidencia', 'cr', 'ncm', 'aliquota', 'inicio_escrituracao'], 'permissions': (('can_view_efdreinf_codigos_atividades_produtos_servicos_cprb', 'Can view efdreinf_codigos_atividades_produtos_servicos_cprb'),)},
        ),
        migrations.AlterModelOptions(
            name='efdreinfeventos',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_efdreinf_eventos', 'Can view efdreinf_eventos'),)},
        ),
        migrations.AlterModelOptions(
            name='efdreinfinformacoesbeneficiariosexterior',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_efdreinf_informacoes_beneficiarios_exterior', 'Can view efdreinf_informacoes_beneficiarios_exterior'),)},
        ),
        migrations.AlterModelOptions(
            name='efdreinfpagamentoscodigos',
            options={'managed': True, 'ordering': ['grupo', 'codigo', 'beneficiario_pj', 'beneficiario_pf', 'descricao'], 'permissions': (('can_view_efdreinf_pagamentos_codigos', 'Can view efdreinf_pagamentos_codigos'),)},
        ),
        migrations.AlterModelOptions(
            name='efdreinfpaises',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_efdreinf_paises', 'Can view efdreinf_paises'),)},
        ),
        migrations.AlterModelOptions(
            name='efdreinfregraspagamentoscodigos',
            options={'managed': True, 'ordering': ['classificacao', 'codigo', 'decimo_terceiro', 'deducoes', 'rendimentos_isentos', 'compensacao_imposto_por_decisao_judicial', 'tributacao_com_exigibilidade_suspensa', 'descricao'], 'permissions': (('can_view_efdreinf_regras_pagamentos_codigos', 'Can view efdreinf_regras_pagamentos_codigos'),)},
        ),
        migrations.AlterModelOptions(
            name='efdreinfrendimentosbeneficiariosexterior',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_efdreinf_rendimentos_beneficiarios_exterior', 'Can view efdreinf_rendimentos_beneficiarios_exterior'),)},
        ),
        migrations.AlterModelOptions(
            name='efdreinfrendimentosbeneficiariosexteriortributacao',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_efdreinf_rendimentos_beneficiarios_exterior_tributacao', 'Can view efdreinf_rendimentos_beneficiarios_exterior_tributacao'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialacidentessituacoesgeradoras',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_acidentes_situacoes_geradoras', 'Can view esocial_acidentes_situacoes_geradoras'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialafastamentosmotivos',
            options={'managed': True, 'ordering': ['codigo', 'descricao', 'data_inicio', 'data_termino'], 'permissions': (('can_view_esocial_afastamentos_motivos', 'Can view esocial_afastamentos_motivos'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialagentescausadoresacidentestrabalho',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_agentes_causadores_acidentes_trabalho', 'Can view esocial_agentes_causadores_acidentes_trabalho'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialagentescausadoresdoencasprofissionais',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_agentes_causadores_doencas_profissionais', 'Can view esocial_agentes_causadores_doencas_profissionais'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialarquivosesocialtipos',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_arquivos_esocial_tipos', 'Can view esocial_arquivos_esocial_tipos'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialatividadespericulosasinsalubresespeciais',
            options={'managed': True, 'ordering': ['grupo', 'codigo', 'descricao'], 'permissions': (('can_view_esocial_atividades_periculosas_insalubres_especiais', 'Can view esocial_atividades_periculosas_insalubres_especiais'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialbeneficiosprevidenciarioscessacaomotivos',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_beneficios_previdenciarios_cessacao_motivos', 'Can view esocial_beneficios_previdenciarios_cessacao_motivos'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialbeneficiosprevidenciariostipos',
            options={'managed': True, 'ordering': ['grupo', 'codigo', 'descricao'], 'permissions': (('can_view_esocial_beneficios_previdenciarios_tipos', 'Can view esocial_beneficios_previdenciarios_tipos'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialclassificacoestributarias',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_classificacoes_tributarias', 'Can view esocial_classificacoes_tributarias'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialcodificacoesacidentetrabalho',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_codificacoes_acidente_trabalho', 'Can view esocial_codificacoes_acidente_trabalho'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialcodigoaliquotasfpasterceiros',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_codigo_aliquotas_fpas_terceiros', 'Can view esocial_codigo_aliquotas_fpas_terceiros'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialcompatibilidadescategoriasclassificacoeslotacoes',
            options={'managed': True, 'ordering': ['codigo', 'classificacao_tributaria'], 'permissions': (('can_view_esocial_compatibilidades_categorias_classificacoes_lotacoes', 'Can view esocial_compatibilidades_categorias_classificacoes_lotacoes'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialcompatibilidadesfpasclassificacoestributarias',
            options={'managed': True, 'ordering': ['codigo'], 'permissions': (('can_view_esocial_compatibilidades_fpas_classificacoes_tributarias', 'Can view esocial_compatibilidades_fpas_classificacoes_tributarias'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialcompatibilidadeslotacoesclassificacoes',
            options={'managed': True, 'ordering': ['codigo'], 'permissions': (('can_view_esocial_compatibilidades_lotacoes_classificacoes', 'Can view esocial_compatibilidades_lotacoes_classificacoes'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialdependentestipos',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_dependentes_tipos', 'Can view esocial_dependentes_tipos'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialdesligamentosmotivos',
            options={'managed': True, 'ordering': ['codigo', 'descricao', 'data_inicio', 'data_termino'], 'permissions': (('can_view_esocial_desligamentos_motivos', 'Can view esocial_desligamentos_motivos'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialfatoresrisco',
            options={'managed': True, 'ordering': ['grupo', 'codigo', 'descricao'], 'permissions': (('can_view_esocial_fatores_risco', 'Can view esocial_fatores_risco'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialfinanciamentosaposentadoriasespeciais',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_financiamentos_aposentadorias_especiais', 'Can view esocial_financiamentos_aposentadorias_especiais'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialinscricoestipos',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_inscricoes_tipos', 'Can view esocial_inscricoes_tipos'),)},
        ),
        migrations.AlterModelOptions(
            name='esociallogradourostipos',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_logradouros_tipos', 'Can view esocial_logradouros_tipos'),)},
        ),
        migrations.AlterModelOptions(
            name='esociallotacoestributariastipos',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_lotacoes_tributarias_tipos', 'Can view esocial_lotacoes_tributarias_tipos'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialnaturezasjuridicas',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_naturezas_juridicas', 'Can view esocial_naturezas_juridicas'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialnaturezaslesoes',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_naturezas_lesoes', 'Can view esocial_naturezas_lesoes'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialnaturezasrubricas',
            options={'managed': True, 'ordering': ['codigo', 'titulo'], 'permissions': (('can_view_esocial_naturezas_rubricas', 'Can view esocial_naturezas_rubricas'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialpaises',
            options={'managed': True, 'ordering': ['codigo', 'nome'], 'permissions': (('can_view_esocial_paises', 'Can view esocial_paises'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialpartescorpoatingidas',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_partes_corpo_atingidas', 'Can view esocial_partes_corpo_atingidas'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialprocedimentosdiagnosticos',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_procedimentos_diagnosticos', 'Can view esocial_procedimentos_diagnosticos'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialprogramasplanosdocumentos',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_programas_planos_documentos', 'Can view esocial_programas_planos_documentos'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialtrabalhadorescategorias',
            options={'managed': True, 'ordering': ['grupo', 'codigo', 'descricao'], 'permissions': (('can_view_esocial_trabalhadores_categorias', 'Can view esocial_trabalhadores_categorias'),)},
        ),
        migrations.AlterModelOptions(
            name='esocialtreinamentoscapacitacoesexerciciossimulados',
            options={'managed': True, 'ordering': ['codigo', 'descricao'], 'permissions': (('can_view_esocial_treinamentos_capacitacoes_exercicios_simulados', 'Can view esocial_treinamentos_capacitacoes_exercicios_simulados'),)},
        ),
        migrations.AlterModelOptions(
            name='municipios',
            options={'managed': True, 'ordering': ['titulo'], 'permissions': (('can_view_municipios', 'Can view municipios'),)},
        ),
    ]
