# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mensageiro', '0015_auto_20190204_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arquivos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='arquivos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='arquivos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='importacaoarquivos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='importacaoarquivos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='importacaoarquivos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='importacaoarquivos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='importacaoarquivoseventos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='importacaoarquivoseventos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='importacaoarquivoseventos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='importacaoarquivoseventos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='regrasdevalidacao',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regrasdevalidacao_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='regrasdevalidacao',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='regrasdevalidacao_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='relatorios',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relatorios_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='relatorios',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relatorios_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='retornoseventos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retornoseventos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='retornoseventos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retornoseventos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='retornoseventoshorarios',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retornoseventoshorarios_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='retornoseventoshorarios',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retornoseventoshorarios_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='retornoseventosintervalos',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retornoseventosintervalos_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='retornoseventosintervalos',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retornoseventosintervalos_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='retornoseventosocorrencias',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retornoseventosocorrencias_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='retornoseventosocorrencias',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='retornoseventosocorrencias_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transmissorlote_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transmissorlote',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transmissorlote_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transmissorloteefdreinf',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transmissorloteefdreinf_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transmissorloteefdreinf',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transmissorloteefdreinf_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transmissorloteefdreinfocorrencias',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transmissorloteefdreinfocorrencias_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transmissorloteefdreinfocorrencias',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transmissorloteefdreinfocorrencias_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transmissorloteesocial',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transmissorloteesocial_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transmissorloteesocial',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transmissorloteesocial_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transmissorloteesocialocorrencias',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transmissorloteesocialocorrencias_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transmissorloteesocialocorrencias',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transmissorloteesocialocorrencias_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]