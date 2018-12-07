# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-23 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0008_auto_20181120_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importacaoarquivos',
            name='arquivo',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='importacaoarquivos',
            name='data_hora',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='importacaoarquivos',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Aguardando!'), (1, 'Sucesso!'), (2, 'Erro!'), (3, 'Arquivo inv\xe1lido!'), (5, 'Identidade do evento j\xe1 est\xe1 cadastrada em nossa base'), (6, 'Processado'), (7, 'Processando'), (8, 'Processado com erros'), (9, 'Vers\xe3o incompat\xedvel')]),
        ),
        migrations.AlterField(
            model_name='importacaoarquivoseventos',
            name='importacao_arquivos',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='importacaoarquivoseventos_importacao_arquivos', to='mensageiro.ImportacaoArquivos'),
        ),
        migrations.AlterField(
            model_name='regrasdevalidacao',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='regrasdevalidacao',
            name='obrigatorio',
            field=models.IntegerField(blank=True, choices=[(0, 'N\xe3o'), (1, 'Sim')]),
        ),
        migrations.AlterField(
            model_name='regrasdevalidacao',
            name='versao',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='retornoseventosocorrencias',
            name='codigo',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='retornoseventosocorrencias',
            name='descricao',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='retornoseventosocorrencias',
            name='retornos_eventos',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='retornoseventosocorrencias_retornos_eventos', to='mensageiro.RetornosEventos'),
        ),
        migrations.AlterField(
            model_name='retornoseventosocorrencias',
            name='tipo',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Erro'), (2, '2 - Advert\xeancia')]),
        ),
        migrations.AlterField(
            model_name='transmissorloteefdreinf',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (5, 'Erro no envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')], default=0),
        ),
        migrations.AlterField(
            model_name='transmissorloteesocial',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Cadastrado'), (5, 'Erro no envio'), (7, 'Enviado'), (8, 'Erro na consulta'), (9, 'Consultado')], default=0),
        ),
    ]