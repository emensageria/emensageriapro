#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"


"""

    eMensageria - Sistema Open-Source de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
    Copyright (C) 2018  Marcelo Medeiros de Vasconcellos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation, either version 3 of the
    License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

        Este programa é distribuído na esperança de que seja útil,
        mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
        COMERCIABILIDADE OU ADEQUAÇÃO A UM DETERMINADO FIM. Veja o
        Licença Pública Geral GNU Affero para mais detalhes.

        Este programa é software livre: você pode redistribuí-lo e / ou modificar
        sob os termos da licença GNU Affero General Public License como
        publicado pela Free Software Foundation, seja versão 3 do
        Licença, ou (a seu critério) qualquer versão posterior.

        Você deveria ter recebido uma cópia da Licença Pública Geral GNU Affero
        junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.

"""


import datetime
import json
import base64
from django.contrib import messages
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from django.forms.models import model_to_dict
from wkhtmltopdf.views import PDFTemplateResponse
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from emensageriapro.padrao import *
from emensageriapro.tabelas.forms import *
from emensageriapro.tabelas.models import *
from emensageriapro.controle_de_acesso.models import *
from emensageriapro.esocial.models import s2200evtAdmissao
from emensageriapro.esocial.forms import form_s2200_evtadmissao
from emensageriapro.esocial.models import s2206evtAltContratual
from emensageriapro.esocial.forms import form_s2206_evtaltcontratual
from emensageriapro.esocial.models import s2210evtCAT
from emensageriapro.esocial.forms import form_s2210_evtcat
from emensageriapro.esocial.models import s2220evtMonit
from emensageriapro.esocial.forms import form_s2220_evtmonit
from emensageriapro.esocial.models import s2221evtToxic
from emensageriapro.esocial.forms import form_s2221_evttoxic
from emensageriapro.esocial.models import s2230evtAfastTemp
from emensageriapro.esocial.forms import form_s2230_evtafasttemp
from emensageriapro.esocial.models import s2240evtExpRisco
from emensageriapro.esocial.forms import form_s2240_evtexprisco
from emensageriapro.esocial.models import s2245evtTreiCap
from emensageriapro.esocial.forms import form_s2245_evttreicap
from emensageriapro.esocial.models import s2300evtTSVInicio
from emensageriapro.esocial.forms import form_s2300_evttsvinicio
from emensageriapro.esocial.models import s2306evtTSVAltContr
from emensageriapro.esocial.forms import form_s2306_evttsvaltcontr
from emensageriapro.esocial.models import s2399evtTSVTermino
from emensageriapro.esocial.forms import form_s2399_evttsvtermino
from emensageriapro.s1200.models import s1200remunOutrEmpr
from emensageriapro.s1200.forms import form_s1200_remunoutrempr
from emensageriapro.s1200.models import s1200dmDev
from emensageriapro.s1200.forms import form_s1200_dmdev
from emensageriapro.s1202.models import s1202dmDev
from emensageriapro.s1202.forms import form_s1202_dmdev
from emensageriapro.s1202.models import s1202infoPerApurremunPerApur
from emensageriapro.s1202.forms import form_s1202_infoperapur_remunperapur
from emensageriapro.s1202.models import s1202infoPerAntremunPerAnt
from emensageriapro.s1202.forms import form_s1202_infoperant_remunperant
from emensageriapro.s1210.models import s1210detPgtoFer
from emensageriapro.s1210.forms import form_s1210_detpgtofer
from emensageriapro.s1210.models import s1210detPgtoAnt
from emensageriapro.s1210.forms import form_s1210_detpgtoant
from emensageriapro.s2299.models import s2299infoTrabIntermremunOutrEmpr
from emensageriapro.s2299.forms import form_s2299_infotrabinterm_remunoutrempr
from emensageriapro.s2399.models import s2399remunOutrEmpr
from emensageriapro.s2399.forms import form_s2399_remunoutrempr
from emensageriapro.s5001.models import s5001infoCategIncid
from emensageriapro.s5001.forms import form_s5001_infocategincid
from emensageriapro.s5002.models import s5002infoIrrf
from emensageriapro.s5002.forms import form_s5002_infoirrf
from emensageriapro.s5003.models import s5003infoTrabFGTS
from emensageriapro.s5003.forms import form_s5003_infotrabfgts
from emensageriapro.s5003.models import s5003infoTrabDps
from emensageriapro.s5003.forms import form_s5003_infotrabdps
from emensageriapro.s5011.models import s5011basesRemun
from emensageriapro.s5011.forms import form_s5011_basesremun



@login_required
def salvar(request, hash):

    try: 
        usuario_id = request.user.id 
        dict_hash = get_hash_url( hash )
        esocial_trabalhadores_categorias_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys(): 
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except: 
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios, id = usuario_id)
    pagina = ConfigPaginas.objects.get( endereco='esocial_trabalhadores_categorias')
    permissao = ConfigPermissoes.objects.get( config_paginas=pagina, config_perfis=usuario.config_perfis)
    if esocial_trabalhadores_categorias_id:
        esocial_trabalhadores_categorias = get_object_or_404(eSocialTrabalhadoresCategorias, id = esocial_trabalhadores_categorias_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    if permissao.permite_visualizar:
        mensagem = None
        if esocial_trabalhadores_categorias_id:
            esocial_trabalhadores_categorias_form = form_esocial_trabalhadores_categorias(request.POST or None, instance = esocial_trabalhadores_categorias, 
                                         initial = {'excluido': False})
        else:
            esocial_trabalhadores_categorias_form = form_esocial_trabalhadores_categorias(request.POST or None,
                                         initial = {'excluido': False})
        if request.method == 'POST':
            if esocial_trabalhadores_categorias_form.is_valid():
            
                dados = esocial_trabalhadores_categorias_form.cleaned_data
                obj = esocial_trabalhadores_categorias_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                
                if not esocial_trabalhadores_categorias_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                 'esocial_trabalhadores_categorias', obj.id, usuario_id, 1)
                else:
                
                    gravar_auditoria(json.dumps(model_to_dict(esocial_trabalhadores_categorias), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str), 
                                     'esocial_trabalhadores_categorias', esocial_trabalhadores_categorias_id, usuario_id, 2)
                                     
                if request.session['retorno_pagina'] not in ('esocial_trabalhadores_categorias_apagar', 'esocial_trabalhadores_categorias_salvar', 'esocial_trabalhadores_categorias'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if esocial_trabalhadores_categorias_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('esocial_trabalhadores_categorias_salvar', hash=url_hash)
            else:
                messages.error(request, u'Erro ao salvar!')
        esocial_trabalhadores_categorias_form = disabled_form_fields(esocial_trabalhadores_categorias_form, permissao.permite_editar)
        
        #esocial_trabalhadores_categorias_campos_multiple_passo3
        
        if int(dict_hash['print']):
            esocial_trabalhadores_categorias_form = disabled_form_for_print(esocial_trabalhadores_categorias_form)
            
        #esocial_trabalhadores_categorias_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'esocial_trabalhadores_categorias' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'esocial_trabalhadores_categorias_salvar'
        context = {
            'esocial_trabalhadores_categorias': esocial_trabalhadores_categorias, 
            'esocial_trabalhadores_categorias_form': esocial_trabalhadores_categorias_form, 
            'mensagem': mensagem, 
            'esocial_trabalhadores_categorias_id': int(esocial_trabalhadores_categorias_id),
            'usuario': usuario, 
            
            'hash': hash, 
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #esocial_trabalhadores_categorias_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 'esocial_trabalhadores_categorias_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='esocial_trabalhadores_categorias_salvar.html',
                filename="esocial_trabalhadores_categorias.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('esocial_trabalhadores_categorias_salvar.html', context)
            filename = "esocial_trabalhadores_categorias.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response

    else:
        context = {
            'usuario': usuario, 
            
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
           
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)