# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('s2205', '0012_auto_20190513_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='s2205aposentadoria',
            name='s2205_evtaltcadastral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205aposentadoria_s2205_evtaltcadastral', to='esocial.s2205evtAltCadastral'),
        ),
        migrations.AlterField(
            model_name='s2205aposentadoria',
            name='trabaposent',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2205brasil',
            name='cep',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='s2205brasil',
            name='codmunic',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='s2205brasil',
            name='dsclograd',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='s2205brasil',
            name='nrlograd',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='s2205brasil',
            name='s2205_evtaltcadastral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205brasil_s2205_evtaltcadastral', to='esocial.s2205evtAltCadastral'),
        ),
        migrations.AlterField(
            model_name='s2205brasil',
            name='tplograd',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='s2205brasil',
            name='uf',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s2205cnh',
            name='categoriacnh',
            field=models.CharField(choices=[(b'A', 'A'), (b'AB', 'AB'), (b'AC', 'AC'), (b'AD', 'AD'), (b'AE', 'AE'), (b'B', 'B'), (b'C', 'C'), (b'D', 'D'), (b'E', 'E')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s2205cnh',
            name='dtvalid',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s2205cnh',
            name='nrregcnh',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='s2205cnh',
            name='s2205_documentos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205cnh_s2205_documentos', to='s2205.s2205documentos'),
        ),
        migrations.AlterField(
            model_name='s2205cnh',
            name='ufcnh',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s2205contato',
            name='s2205_evtaltcadastral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205contato_s2205_evtaltcadastral', to='esocial.s2205evtAltCadastral'),
        ),
        migrations.AlterField(
            model_name='s2205ctps',
            name='nrctps',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='s2205ctps',
            name='s2205_documentos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205ctps_s2205_documentos', to='s2205.s2205documentos'),
        ),
        migrations.AlterField(
            model_name='s2205ctps',
            name='seriectps',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='s2205ctps',
            name='ufctps',
            field=models.CharField(choices=[(b'AC', 'Acre'), (b'AL', 'Alagoas'), (b'AM', 'Amazonas'), (b'AP', 'Amap\xe1'), (b'BA', 'Bahia'), (b'CE', 'Cear\xe1'), (b'DF', 'Distrito Federal'), (b'ES', 'Esp\xedrito Santo'), (b'GO', 'Goi\xe1s'), (b'MA', 'Maranh\xe3o'), (b'MG', 'Minas Gerais'), (b'MS', 'Mato Grosso do Sul'), (b'MT', 'Mato Grosso'), (b'PA', 'Par\xe1'), (b'PB', 'Para\xedba'), (b'PE', 'Pernambuco'), (b'PI', 'Piau\xed'), (b'PR', 'Paran\xe1'), (b'RJ', 'Rio de Janeiro'), (b'RN', 'Rio Grande do Norte'), (b'RO', 'Rond\xf4nia'), (b'RR', 'Roraima'), (b'RS', 'Rio Grande do Sul'), (b'SC', 'Santa Catarina'), (b'SE', 'Sergipe'), (b'SP', 'S\xe3o Paulo'), (b'TO', 'Tocantins')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s2205dependente',
            name='depirrf',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2205dependente',
            name='depsf',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2205dependente',
            name='dtnascto',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='s2205dependente',
            name='inctrab',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2205dependente',
            name='nmdep',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='s2205dependente',
            name='s2205_evtaltcadastral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205dependente_s2205_evtaltcadastral', to='esocial.s2205evtAltCadastral'),
        ),
        migrations.AlterField(
            model_name='s2205dependente',
            name='tpdep',
            field=models.CharField(choices=[(b'01', '01 - C\xf4njuge'), (b'02', '02 - Companheiro(a) com o(a) qual tenha filho ou viva h\xe1 mais de 5 (cinco) anos ou possua Declara\xe7\xe3o de Uni\xe3o Est\xe1vel'), (b'03', '03 - Filho(a) ou enteado(a)'), (b'04', '04 - Filho(a) ou enteado(a), universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xba grau'), (b'06', '06 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial'), (b'07', '07 - Irm\xe3o(\xe3), neto(a) ou bisneto(a) sem arrimo dos pais, universit\xe1rio(a) ou cursando escola t\xe9cnica de 2\xb0 grau, do(a) qual detenha a guarda judicial'), (b'09', '09 - Pais, av\xf3s e bisav\xf3s'), (b'10', '10 - Menor pobre do qual detenha a guarda judicial'), (b'11', '11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador'), (b'12', '12 - Ex-c\xf4njuge'), (b'99', '99 - Agregado/Outros')], max_length=2),
        ),
        migrations.AlterField(
            model_name='s2205documentos',
            name='s2205_evtaltcadastral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205documentos_s2205_evtaltcadastral', to='esocial.s2205evtAltCadastral'),
        ),
        migrations.AlterField(
            model_name='s2205exterior',
            name='dsclograd',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='s2205exterior',
            name='nmcid',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='s2205exterior',
            name='nrlograd',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='s2205exterior',
            name='paisresid',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='s2205exterior',
            name='s2205_evtaltcadastral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205exterior_s2205_evtaltcadastral', to='esocial.s2205evtAltCadastral'),
        ),
        migrations.AlterField(
            model_name='s2205infodeficiencia',
            name='defauditiva',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2205infodeficiencia',
            name='deffisica',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2205infodeficiencia',
            name='defintelectual',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2205infodeficiencia',
            name='defmental',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2205infodeficiencia',
            name='defvisual',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2205infodeficiencia',
            name='reabreadap',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2205infodeficiencia',
            name='s2205_evtaltcadastral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205infodeficiencia_s2205_evtaltcadastral', to='esocial.s2205evtAltCadastral'),
        ),
        migrations.AlterField(
            model_name='s2205oc',
            name='nroc',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='s2205oc',
            name='orgaoemissor',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='s2205oc',
            name='s2205_documentos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205oc_s2205_documentos', to='s2205.s2205documentos'),
        ),
        migrations.AlterField(
            model_name='s2205rg',
            name='nrrg',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='s2205rg',
            name='orgaoemissor',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='s2205rg',
            name='s2205_documentos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205rg_s2205_documentos', to='s2205.s2205documentos'),
        ),
        migrations.AlterField(
            model_name='s2205ric',
            name='nrric',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='s2205ric',
            name='orgaoemissor',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='s2205ric',
            name='s2205_documentos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205ric_s2205_documentos', to='s2205.s2205documentos'),
        ),
        migrations.AlterField(
            model_name='s2205rne',
            name='nrrne',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='s2205rne',
            name='orgaoemissor',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='s2205rne',
            name='s2205_documentos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205rne_s2205_documentos', to='s2205.s2205documentos'),
        ),
        migrations.AlterField(
            model_name='s2205trabestrangeiro',
            name='casadobr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2205trabestrangeiro',
            name='classtrabestrang',
            field=models.IntegerField(choices=[(1, '1 - Visto permanente'), (10, '10 - Beneficiado pelo acordo entre pa\xedses do Mercosul'), (11, '11 - Dependente de agente diplom\xe1tico e/ou consular de pa\xedses que mant\xe9m conv\xeanio de reciprocidade para o exerc\xedcio de atividade remunerada no Brasil'), (12, '12 - Beneficiado pelo Tratado de Amizade, Coopera\xe7\xe3o e Consulta entre a Rep\xfablica Federativa do Brasil e a Rep\xfablica Portuguesa.'), (2, '2 - Visto tempor\xe1rio'), (3, '3 - Asilado'), (4, '4 - Refugiado'), (5, '5 - Solicitante de Ref\xfagio'), (6, '6 - Residente fora do Brasil'), (7, '7 - Deficiente f\xedsico e com mais de 51 anos'), (8, '8 - Com resid\xeancia provis\xf3ria e anistiado, em situa\xe7\xe3o irregular'), (9, '9 - Perman\xeancia no Brasil em raz\xe3o de filhos ou c\xf4njuge brasileiros')]),
        ),
        migrations.AlterField(
            model_name='s2205trabestrangeiro',
            name='filhosbr',
            field=models.CharField(choices=[(b'N', 'N - N\xe3o.'), (b'S', 'S - Sim')], max_length=1),
        ),
        migrations.AlterField(
            model_name='s2205trabestrangeiro',
            name='s2205_evtaltcadastral',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='s2205trabestrangeiro_s2205_evtaltcadastral', to='esocial.s2205evtAltCadastral'),
        ),
    ]