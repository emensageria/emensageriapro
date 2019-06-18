# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-14 21:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0032_auto_20190606_2116'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificados',
            options={'managed': True, 'ordering': ['nome'], 'permissions': (('can_view_certificados', 'Can view certificados'),), 'verbose_name': 'Certificados', 'verbose_name_plural': 'Certificados'},
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='contribuinte_nrinsc',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='contribuinte_tpinsc',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='efdreinf_certificado',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='efdreinf_intervalo',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='efdreinf_lote_max',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='efdreinf_lote_min',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='efdreinf_pasta',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='efdreinf_tempo_prox_envio',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='efdreinf_timeout',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='envio_automatico',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='esocial_intervalo',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='esocial_lote_max',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='esocial_lote_min',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='esocial_pasta',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='esocial_tempo_prox_envio',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='esocial_timeout',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='validar_eventos',
        ),
        migrations.RemoveField(
            model_name='transmissorlote',
            name='verificar_predecessao',
        ),
    ]