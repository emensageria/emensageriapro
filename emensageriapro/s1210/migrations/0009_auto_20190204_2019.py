# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s1210', '0008_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s1210deps',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210deps',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoant',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoant',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoantinfopgtoant',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoantinfopgtoant',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtobenpr',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtobenpr',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtobenprinfopgtoparc',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtobenprinfopgtoparc',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtobenprretpgtotot',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtobenprretpgtotot',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtofer',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtofer',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoferdetrubrfer',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoferdetrubrfer',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoferpenalim',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoferpenalim',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtofl',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtofl',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoflinfopgtoparc',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoflinfopgtoparc',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoflpenalim',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoflpenalim',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoflretpgtotot',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210detpgtoflretpgtotot',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210idepgtoext',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210idepgtoext',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s1210infopgto',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s1210infopgto',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='s1210deps',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210deps',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoant',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoant',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoantinfopgtoant',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoantinfopgtoant',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenpr',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenpr',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprinfopgtoparc',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprinfopgtoparc',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprretpgtotot',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtobenprretpgtotot',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofer',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofer',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferdetrubrfer',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferdetrubrfer',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferpenalim',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoferpenalim',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofl',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtofl',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflinfopgtoparc',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflinfopgtoparc',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflpenalim',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflpenalim',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflretpgtotot',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210detpgtoflretpgtotot',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210idepgtoext',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210idepgtoext',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210infopgto',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s1210infopgto',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
