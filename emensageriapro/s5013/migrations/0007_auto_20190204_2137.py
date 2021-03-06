# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('s5013', '0006_auto_20190204_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='s5013baseperante',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013baseperante_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s5013baseperante',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013baseperante_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s5013baseperapur',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013baseperapur_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s5013baseperapur',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013baseperapur_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s5013dpsperante',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013dpsperante_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s5013dpsperante',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013dpsperante_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s5013dpsperapur',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013dpsperapur_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s5013dpsperapur',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013dpsperapur_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s5013infobaseperante',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013infobaseperante_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s5013infobaseperante',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013infobaseperante_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s5013infodpsperante',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013infodpsperante_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s5013infodpsperante',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s5013infodpsperante_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]
