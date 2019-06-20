# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 12:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('r4020', '0008_auto_20190602_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='r4020cofins',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020cofins',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020cofins',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020cofins_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020csll',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020csll',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020csll',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020csll_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020despprocjud',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020despprocjud',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020despprocjud',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020despprocjud_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020fci',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020fci',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020fci',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020fci_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020ideadv',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020ideadv',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020ideadv',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020ideadv_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020idepgto',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020idepgto',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020idepgto',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020idepgto_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020infopgto',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020infopgto',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020infopgto',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020infopgto_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020infopgtoext',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020infopgtoext',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020infopgtoext',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020infopgtoext_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020infoprocjud',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020infoprocjud',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020infoprocjud',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020infoprocjud_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020infoprocret',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020infoprocret',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020infoprocret',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020infoprocret_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020ir',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020ir',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020ir',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020ir_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020origemrec',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020origemrec',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020origemrec',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020origemrec_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020pp',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020pp',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020pp',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020pp_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='r4020scp',
            name='ativo',
            field=models.NullBooleanField(default=True),
        ),
        migrations.AddField(
            model_name='r4020scp',
            name='desativado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='r4020scp',
            name='desativado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020scp_desativado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]