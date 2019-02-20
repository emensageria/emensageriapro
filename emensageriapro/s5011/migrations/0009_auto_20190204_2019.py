# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('s5011', '0008_auto_20190204_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='s5011basesaquis',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011basesaquis',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011basesavnport',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011basesavnport',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011basescomerc',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011basescomerc',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011basesremun',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011basesremun',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011dadosopport',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011dadosopport',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011ideestab',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011ideestab',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011idelotacao',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011idelotacao',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infoatconc',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infoatconc',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infocomplobra',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infocomplobra',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infocpseg',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infocpseg',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infocrcontrib',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infocrcontrib',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infocrestab',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infocrestab',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infoemprparcial',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infoemprparcial',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infoestab',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infoestab',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infopj',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infopj',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infosubstpatropport',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infosubstpatropport',
            name='modificado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infotercsusp',
            name='criado_por',
        ),
        migrations.RemoveField(
            model_name='s5011infotercsusp',
            name='modificado_por',
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011basesaquis',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011basesavnport',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011basesavnport',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011basescomerc',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011basescomerc',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011basesremun',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011dadosopport',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011dadosopport',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011ideestab',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011ideestab',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011idelotacao',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011idelotacao',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infoatconc',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infoatconc',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infocomplobra',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infocomplobra',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infocpseg',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infocpseg',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infocrcontrib',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infocrcontrib',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infocrestab',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infocrestab',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infoemprparcial',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infoemprparcial',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infoestab',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infoestab',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infopj',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infopj',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infosubstpatropport',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infosubstpatropport',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infotercsusp',
            name='criado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='s5011infotercsusp',
            name='modificado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]