# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-07 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mensageiro', '0042_auto_20190807_2059'),
        ('efdreinf', '0028_auto_20190622_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='r1000evtinfocontri',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1000evtinfocontri_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r1070evttabprocesso',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r1070evttabprocesso_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r2010evtservtom',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r2010evtservtom_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r2020evtservprest',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r2020evtservprest_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r2030evtassocdesprec',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r2030evtassocdesprec_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r2040evtassocdesprep',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r2040evtassocdesprep_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r2050evtcomprod',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r2050evtcomprod_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r2060evtcprb',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r2060evtcprb_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r2070evtpgtosdivs',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r2070evtpgtosdivs_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r2098evtreabreevper',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r2098evtreabreevper_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r2099evtfechaevper',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r2099evtfechaevper_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r3010evtespdesportivo',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r3010evtespdesportivo_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r4010evtretpf',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4010evtretpf_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r4020evtretpj',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4020evtretpj_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r4040evtbenefnid',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4040evtbenefnid_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r4098evtreab',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4098evtreab_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r4099evtfech',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4099evtfech_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r5001evttotal',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r5001evttotal_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r5011evttotalcontrib',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r5011evttotalcontrib_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r9000evtexclusao',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9000evtexclusao_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r9001evttotal',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9001evttotal_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r9002evtret',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9002evtret_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r9011evttotalcontrib',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9011evttotalcontrib_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
        migrations.AddField(
            model_name='r9012evtretcons',
            name='transmissor_lote_efdreinf_error',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r9012evtretcons_transmissor_lote_efdreinf_error', to='mensageiro.TransmissorLoteEfdreinf'),
        ),
    ]
