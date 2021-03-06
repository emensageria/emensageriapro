# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 11:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('controle_de_acesso', '0024_auto_20190618_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditoria',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auditoria_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='configperfis',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='configperfis',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='configperfis',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='configperfis_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]
