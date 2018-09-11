#coding:utf-8
from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
    # Examples:



url(r'^s1005-inclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao.apagar', 
        name='s1005_inclusao_apagar'),

url(r'^s1005-inclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao.listar', 
        name='s1005_inclusao'),

url(r'^s1005-inclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao.salvar', 
        name='s1005_inclusao_salvar'),



url(r'^s1005-inclusao-procadmjudrat/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_procadmjudrat.apagar', 
        name='s1005_inclusao_procadmjudrat_apagar'),

url(r'^s1005-inclusao-procadmjudrat/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_procadmjudrat.listar', 
        name='s1005_inclusao_procadmjudrat'),

url(r'^s1005-inclusao-procadmjudrat/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_procadmjudrat.salvar', 
        name='s1005_inclusao_procadmjudrat_salvar'),



url(r'^s1005-inclusao-procadmjudfap/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_procadmjudfap.apagar', 
        name='s1005_inclusao_procadmjudfap_apagar'),

url(r'^s1005-inclusao-procadmjudfap/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_procadmjudfap.listar', 
        name='s1005_inclusao_procadmjudfap'),

url(r'^s1005-inclusao-procadmjudfap/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_procadmjudfap.salvar', 
        name='s1005_inclusao_procadmjudfap_salvar'),



url(r'^s1005-inclusao-infocaepf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_infocaepf.apagar', 
        name='s1005_inclusao_infocaepf_apagar'),

url(r'^s1005-inclusao-infocaepf/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_infocaepf.listar', 
        name='s1005_inclusao_infocaepf'),

url(r'^s1005-inclusao-infocaepf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_infocaepf.salvar', 
        name='s1005_inclusao_infocaepf_salvar'),



url(r'^s1005-inclusao-infoobra/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_infoobra.apagar', 
        name='s1005_inclusao_infoobra_apagar'),

url(r'^s1005-inclusao-infoobra/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_infoobra.listar', 
        name='s1005_inclusao_infoobra'),

url(r'^s1005-inclusao-infoobra/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_infoobra.salvar', 
        name='s1005_inclusao_infoobra_salvar'),



url(r'^s1005-inclusao-infoenteduc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_infoenteduc.apagar', 
        name='s1005_inclusao_infoenteduc_apagar'),

url(r'^s1005-inclusao-infoenteduc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_infoenteduc.listar', 
        name='s1005_inclusao_infoenteduc'),

url(r'^s1005-inclusao-infoenteduc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_infoenteduc.salvar', 
        name='s1005_inclusao_infoenteduc_salvar'),



url(r'^s1005-inclusao-infopcd/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_infopcd.apagar', 
        name='s1005_inclusao_infopcd_apagar'),

url(r'^s1005-inclusao-infopcd/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_infopcd.listar', 
        name='s1005_inclusao_infopcd'),

url(r'^s1005-inclusao-infopcd/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_inclusao_infopcd.salvar', 
        name='s1005_inclusao_infopcd_salvar'),



url(r'^s1005-alteracao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao.apagar', 
        name='s1005_alteracao_apagar'),

url(r'^s1005-alteracao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao.listar', 
        name='s1005_alteracao'),

url(r'^s1005-alteracao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao.salvar', 
        name='s1005_alteracao_salvar'),



url(r'^s1005-alteracao-procadmjudrat/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_procadmjudrat.apagar', 
        name='s1005_alteracao_procadmjudrat_apagar'),

url(r'^s1005-alteracao-procadmjudrat/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_procadmjudrat.listar', 
        name='s1005_alteracao_procadmjudrat'),

url(r'^s1005-alteracao-procadmjudrat/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_procadmjudrat.salvar', 
        name='s1005_alteracao_procadmjudrat_salvar'),



url(r'^s1005-alteracao-procadmjudfap/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_procadmjudfap.apagar', 
        name='s1005_alteracao_procadmjudfap_apagar'),

url(r'^s1005-alteracao-procadmjudfap/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_procadmjudfap.listar', 
        name='s1005_alteracao_procadmjudfap'),

url(r'^s1005-alteracao-procadmjudfap/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_procadmjudfap.salvar', 
        name='s1005_alteracao_procadmjudfap_salvar'),

)


urlpatterns += patterns('',


url(r'^s1005-alteracao-infocaepf/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_infocaepf.apagar', 
        name='s1005_alteracao_infocaepf_apagar'),

url(r'^s1005-alteracao-infocaepf/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_infocaepf.listar', 
        name='s1005_alteracao_infocaepf'),

url(r'^s1005-alteracao-infocaepf/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_infocaepf.salvar', 
        name='s1005_alteracao_infocaepf_salvar'),



url(r'^s1005-alteracao-infoobra/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_infoobra.apagar', 
        name='s1005_alteracao_infoobra_apagar'),

url(r'^s1005-alteracao-infoobra/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_infoobra.listar', 
        name='s1005_alteracao_infoobra'),

url(r'^s1005-alteracao-infoobra/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_infoobra.salvar', 
        name='s1005_alteracao_infoobra_salvar'),



url(r'^s1005-alteracao-infoenteduc/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_infoenteduc.apagar', 
        name='s1005_alteracao_infoenteduc_apagar'),

url(r'^s1005-alteracao-infoenteduc/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_infoenteduc.listar', 
        name='s1005_alteracao_infoenteduc'),

url(r'^s1005-alteracao-infoenteduc/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_infoenteduc.salvar', 
        name='s1005_alteracao_infoenteduc_salvar'),



url(r'^s1005-alteracao-infopcd/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_infopcd.apagar', 
        name='s1005_alteracao_infopcd_apagar'),

url(r'^s1005-alteracao-infopcd/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_infopcd.listar', 
        name='s1005_alteracao_infopcd'),

url(r'^s1005-alteracao-infopcd/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_infopcd.salvar', 
        name='s1005_alteracao_infopcd_salvar'),



url(r'^s1005-alteracao-novavalidade/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_novavalidade.apagar', 
        name='s1005_alteracao_novavalidade_apagar'),

url(r'^s1005-alteracao-novavalidade/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_novavalidade.listar', 
        name='s1005_alteracao_novavalidade'),

url(r'^s1005-alteracao-novavalidade/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_alteracao_novavalidade.salvar', 
        name='s1005_alteracao_novavalidade_salvar'),



url(r'^s1005-exclusao/apagar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_exclusao.apagar', 
        name='s1005_exclusao_apagar'),

url(r'^s1005-exclusao/listar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_exclusao.listar', 
        name='s1005_exclusao'),

url(r'^s1005-exclusao/salvar/(?P<hash>.*)/$', 
        'emensageriapro.s1005.views.s1005_exclusao.salvar', 
        name='s1005_exclusao_salvar'),





)