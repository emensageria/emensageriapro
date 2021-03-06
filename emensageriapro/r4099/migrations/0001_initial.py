# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-27 16:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('efdreinf', '0016_auto_20190427_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='r4099ideRespInf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmresp', models.CharField(default=b'A', max_length=70)),
                ('cpfresp', models.CharField(default=b'A', max_length=11)),
                ('telefone', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.CharField(blank=True, max_length=60, null=True)),
                ('criado_em', models.DateTimeField(blank=True, null=True)),
                ('modificado_em', models.DateTimeField(blank=True, null=True)),
                ('excluido', models.NullBooleanField(default=False)),
                ('criado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4099iderespinf_criado_por', to=settings.AUTH_USER_MODEL)),
                ('modificado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='r4099iderespinf_modificado_por', to=settings.AUTH_USER_MODEL)),
                ('r4099_evtfech', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='r4099iderespinf_r4099_evtfech', to='efdreinf.r4099evtFech')),
            ],
            options={
                'managed': True,
                'ordering': ['r4099_evtfech', 'nmresp', 'cpfresp'],
                'db_table': 'r4099_iderespinf',
                'permissions': (('can_view_r4099_iderespinf', 'Can view r4099_iderespinf'),),
            },
        ),
    ]
