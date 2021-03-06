# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('esocial', '0024_auto_20190427_1615'),
        ('s2241', '0009_auto_20190204_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='s2241aposentEsp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241aposentesp_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241aposentesp_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('s2241_evtinsapo', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241aposentesp_s2241_evtinsapo', to='esocial.s2241evtInsApo')),
            ],
            options={
                'managed': True,
                'ordering': ['s2241_evtinsapo'],
                'db_table': 's2241_aposentesp',
                'permissions': (('can_view_s2241_aposentesp', 'Can view s2241_aposentesp'),),
            },
        ),
        migrations.CreateModel(
            name='s2241insalPeric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241insalperic_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='s2241insalperic_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('s2241_evtinsapo', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241insalperic_s2241_evtinsapo', to='esocial.s2241evtInsApo')),
            ],
            options={
                'managed': True,
                'ordering': ['s2241_evtinsapo'],
                'db_table': 's2241_insalperic',
                'permissions': (('can_view_s2241_insalperic', 'Can view s2241_insalperic'),),
            },
        ),
        migrations.AlterModelOptions(
            name='s2241altaposentesp',
            options={'managed': True, 'ordering': ['s2241_aposentesp', 'dtaltcondicao'], 'permissions': (('can_view_s2241_altaposentesp', 'Can view s2241_altaposentesp'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241altinsalperic',
            options={'managed': True, 'ordering': ['s2241_insalperic', 'dtaltcondicao'], 'permissions': (('can_view_s2241_altinsalperic', 'Can view s2241_altinsalperic'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241fimaposentesp',
            options={'managed': True, 'ordering': ['s2241_aposentesp', 'dtfimcondicao'], 'permissions': (('can_view_s2241_fimaposentesp', 'Can view s2241_fimaposentesp'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241fiminsalperic',
            options={'managed': True, 'ordering': ['s2241_insalperic', 'dtfimcondicao'], 'permissions': (('can_view_s2241_fiminsalperic', 'Can view s2241_fiminsalperic'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241iniaposentesp',
            options={'managed': True, 'ordering': ['s2241_aposentesp', 'dtinicondicao'], 'permissions': (('can_view_s2241_iniaposentesp', 'Can view s2241_iniaposentesp'),)},
        ),
        migrations.AlterModelOptions(
            name='s2241iniinsalperic',
            options={'managed': True, 'ordering': ['s2241_insalperic', 'dtinicondicao'], 'permissions': (('can_view_s2241_iniinsalperic', 'Can view s2241_iniinsalperic'),)},
        ),
        migrations.RemoveField(
            model_name='s2241altaposentesp',
            name='s2241_evtinsapo',
        ),
        migrations.RemoveField(
            model_name='s2241altinsalperic',
            name='s2241_evtinsapo',
        ),
        migrations.RemoveField(
            model_name='s2241fimaposentesp',
            name='s2241_evtinsapo',
        ),
        migrations.RemoveField(
            model_name='s2241fiminsalperic',
            name='s2241_evtinsapo',
        ),
        migrations.RemoveField(
            model_name='s2241iniaposentesp',
            name='s2241_evtinsapo',
        ),
        migrations.RemoveField(
            model_name='s2241iniinsalperic',
            name='s2241_evtinsapo',
        ),
        migrations.AlterField(
            model_name='s2241altaposentesp',
            name='dtaltcondicao',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2241altaposentespfatrisco',
            name='codfatris',
            field=models.TextField(default=b'A', max_length=10),
        ),
        migrations.AlterField(
            model_name='s2241altaposentespfatrisco',
            name='s2241_altaposentesp_infoamb',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altaposentespfatrisco_s2241_altaposentesp_infoamb', to='s2241.s2241altAposentEspinfoamb'),
        ),
        migrations.AlterField(
            model_name='s2241altaposentespinfoamb',
            name='codamb',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s2241altaposentespinfoamb',
            name='s2241_altaposentesp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altaposentespinfoamb_s2241_altaposentesp', to='s2241.s2241altAposentEsp'),
        ),
        migrations.AlterField(
            model_name='s2241altinsalperic',
            name='dtaltcondicao',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2241altinsalpericfatrisco',
            name='codfatris',
            field=models.TextField(default=b'A', max_length=10),
        ),
        migrations.AlterField(
            model_name='s2241altinsalpericfatrisco',
            name='s2241_altinsalperic_infoamb',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altinsalpericfatrisco_s2241_altinsalperic_infoamb', to='s2241.s2241altInsalPericinfoamb'),
        ),
        migrations.AlterField(
            model_name='s2241altinsalpericinfoamb',
            name='codamb',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s2241altinsalpericinfoamb',
            name='s2241_altinsalperic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altinsalpericinfoamb_s2241_altinsalperic', to='s2241.s2241altInsalPeric'),
        ),
        migrations.AlterField(
            model_name='s2241fimaposentesp',
            name='dtfimcondicao',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2241fimaposentespinfoamb',
            name='codamb',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s2241fimaposentespinfoamb',
            name='s2241_fimaposentesp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241fimaposentespinfoamb_s2241_fimaposentesp', to='s2241.s2241fimAposentEsp'),
        ),
        migrations.AlterField(
            model_name='s2241fiminsalperic',
            name='dtfimcondicao',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2241fiminsalpericinfoamb',
            name='codamb',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s2241fiminsalpericinfoamb',
            name='s2241_fiminsalperic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241fiminsalpericinfoamb_s2241_fiminsalperic', to='s2241.s2241fimInsalPeric'),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentesp',
            name='dtinicondicao',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentespfatrisco',
            name='codfatris',
            field=models.TextField(default=b'A', max_length=10),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentespfatrisco',
            name='s2241_iniaposentesp_infoamb',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniaposentespfatrisco_s2241_iniaposentesp_infoamb', to='s2241.s2241iniAposentEspinfoAmb'),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentespinfoamb',
            name='codamb',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s2241iniaposentespinfoamb',
            name='s2241_iniaposentesp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniaposentespinfoamb_s2241_iniaposentesp', to='s2241.s2241iniAposentEsp'),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalperic',
            name='dtinicondicao',
            field=models.DateField(default=b'1900-01-01'),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalpericfatrisco',
            name='codfatris',
            field=models.TextField(default=b'A', max_length=10),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalpericfatrisco',
            name='s2241_iniinsalperic_infoamb',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniinsalpericfatrisco_s2241_iniinsalperic_infoamb', to='s2241.s2241iniInsalPericinfoAmb'),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalpericinfoamb',
            name='codamb',
            field=models.CharField(default=b'A', max_length=30),
        ),
        migrations.AlterField(
            model_name='s2241iniinsalpericinfoamb',
            name='s2241_iniinsalperic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniinsalpericinfoamb_s2241_iniinsalperic', to='s2241.s2241iniInsalPeric'),
        ),
        migrations.AddField(
            model_name='s2241altaposentesp',
            name='s2241_aposentesp',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altaposentesp_s2241_aposentesp', to='s2241.s2241aposentEsp'),
        ),
        migrations.AddField(
            model_name='s2241altinsalperic',
            name='s2241_insalperic',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241altinsalperic_s2241_insalperic', to='s2241.s2241insalPeric'),
        ),
        migrations.AddField(
            model_name='s2241fimaposentesp',
            name='s2241_aposentesp',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241fimaposentesp_s2241_aposentesp', to='s2241.s2241aposentEsp'),
        ),
        migrations.AddField(
            model_name='s2241fiminsalperic',
            name='s2241_insalperic',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241fiminsalperic_s2241_insalperic', to='s2241.s2241insalPeric'),
        ),
        migrations.AddField(
            model_name='s2241iniaposentesp',
            name='s2241_aposentesp',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniaposentesp_s2241_aposentesp', to='s2241.s2241aposentEsp'),
        ),
        migrations.AddField(
            model_name='s2241iniinsalperic',
            name='s2241_insalperic',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s2241iniinsalperic_s2241_insalperic', to='s2241.s2241insalPeric'),
        ),
    ]
