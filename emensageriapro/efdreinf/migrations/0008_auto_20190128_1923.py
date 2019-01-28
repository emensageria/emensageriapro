# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-28 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('efdreinf', '0007_auto_20181227_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='r1000evtinfocontri',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r1000evtinfocontri',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r1000evtinfocontri',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='r1070evttabprocesso',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r1070evttabprocesso',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r1070evttabprocesso',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='r2010evtservtom',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2010evtservtom',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r2010evtservtom',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='r2020evtservprest',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2020evtservprest',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r2020evtservprest',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='r2030evtassocdesprec',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2030evtassocdesprec',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r2030evtassocdesprec',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='r2040evtassocdesprep',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2040evtassocdesprep',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r2040evtassocdesprep',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='r2050evtcomprod',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2050evtcomprod',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r2050evtcomprod',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='r2060evtcprb',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2060evtcprb',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r2060evtcprb',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='r2070evtpgtosdivs',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2070evtpgtosdivs',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r2070evtpgtosdivs',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='r2098evtreabreevper',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2098evtreabreevper',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r2098evtreabreevper',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='r2099evtfechaevper',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r2099evtfechaevper',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r2099evtfechaevper',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='r3010evtespdesportivo',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r3010evtespdesportivo',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r3010evtespdesportivo',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='r9000evtexclusao',
            name='procemi',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Aplicativo do contribuinte'), (2, '2 - Aplicativo governamental')]),
        ),
        migrations.AlterField(
            model_name='r9000evtexclusao',
            name='tpamb',
            field=models.IntegerField(blank=True, choices=[(1, '1 - Produ\xe7\xe3o'), (2, '2 - Produ\xe7\xe3o restrita')]),
        ),
        migrations.AlterField(
            model_name='r9000evtexclusao',
            name='verproc',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
