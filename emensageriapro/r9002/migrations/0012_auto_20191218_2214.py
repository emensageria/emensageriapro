# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-12-18 22:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('r9002', '0011_auto_20190929_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='r9002infototal',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r9002infototal',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r9002infototal',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r9002infototal',
            name='r9002_evtret',
        ),
        migrations.RemoveField(
            model_name='r9002regocorrs',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r9002regocorrs',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r9002regocorrs',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r9002regocorrs',
            name='r9002_evtret',
        ),
        migrations.RemoveField(
            model_name='r9002totapurdec',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapurdec',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapurdec',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapurdec',
            name='r9002_infototal',
        ),
        migrations.RemoveField(
            model_name='r9002totapurdia',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapurdia',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapurdia',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapurdia',
            name='r9002_infototal',
        ),
        migrations.RemoveField(
            model_name='r9002totapurmen',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapurmen',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapurmen',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapurmen',
            name='r9002_infototal',
        ),
        migrations.RemoveField(
            model_name='r9002totapurqui',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapurqui',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapurqui',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapurqui',
            name='r9002_infototal',
        ),
        migrations.RemoveField(
            model_name='r9002totapursem',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapursem',
            name='desativado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapursem',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='r9002totapursem',
            name='r9002_infototal',
        ),
        migrations.DeleteModel(
            name='r9002infoTotal',
        ),
        migrations.DeleteModel(
            name='r9002regOcorrs',
        ),
        migrations.DeleteModel(
            name='r9002totApurDec',
        ),
        migrations.DeleteModel(
            name='r9002totApurDia',
        ),
        migrations.DeleteModel(
            name='r9002totApurMen',
        ),
        migrations.DeleteModel(
            name='r9002totApurQui',
        ),
        migrations.DeleteModel(
            name='r9002totApurSem',
        ),
    ]