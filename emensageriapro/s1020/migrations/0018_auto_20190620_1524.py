# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-20 15:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('s1020', '0017_auto_20190620_1408'),
        ('controle_de_acesso', '0026_auto_20190620_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s1020alteracao',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s1020alteracaoinfoemprparcial',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s1020alteracaoinfoprocjudterceiros',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s1020alteracaonovavalidade',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s1020alteracaoprocjudterceiro',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s1020exclusao',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s1020inclusao',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s1020inclusaoinfoemprparcial',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s1020inclusaoinfoprocjudterceiros',
            name='excluido',
        ),
        migrations.RemoveField(
            model_name='s1020inclusaoprocjudterceiro',
            name='excluido',
        ),
    ]
