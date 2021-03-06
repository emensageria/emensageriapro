# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 21:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('s2241', '0008_auto_20190204_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='s2241altaposentesp',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altaposentesp_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241altaposentesp',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altaposentesp_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241altaposentespfatrisco',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altaposentespfatrisco_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241altaposentespfatrisco',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altaposentespfatrisco_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241altaposentespinfoamb',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altaposentespinfoamb_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241altaposentespinfoamb',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altaposentespinfoamb_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241altinsalperic',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altinsalperic_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241altinsalperic',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altinsalperic_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241altinsalpericfatrisco',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altinsalpericfatrisco_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241altinsalpericfatrisco',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altinsalpericfatrisco_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241altinsalpericinfoamb',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altinsalpericinfoamb_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241altinsalpericinfoamb',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altinsalpericinfoamb_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241fimaposentesp',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241fimaposentesp_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241fimaposentesp',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241fimaposentesp_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241fimaposentespinfoamb',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241fimaposentespinfoamb_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241fimaposentespinfoamb',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241fimaposentespinfoamb_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241fiminsalperic',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241fiminsalperic_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241fiminsalperic',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241fiminsalperic_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241fiminsalpericinfoamb',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241fiminsalpericinfoamb_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241fiminsalpericinfoamb',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241fiminsalpericinfoamb_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241iniaposentesp',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniaposentesp_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241iniaposentesp',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniaposentesp_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241iniaposentespfatrisco',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniaposentespfatrisco_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241iniaposentespfatrisco',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniaposentespfatrisco_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241iniaposentespinfoamb',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniaposentespinfoamb_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241iniaposentespinfoamb',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniaposentespinfoamb_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241iniinsalperic',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniinsalperic_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241iniinsalperic',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniinsalperic_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241iniinsalpericfatrisco',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniinsalpericfatrisco_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241iniinsalpericfatrisco',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniinsalpericfatrisco_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241iniinsalpericinfoamb',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniinsalpericinfoamb_criado_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='s2241iniinsalpericinfoamb',
            name='modificado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniinsalpericinfoamb_modificado_por', to=settings.AUTH_USER_MODEL),
        ),
    ]
