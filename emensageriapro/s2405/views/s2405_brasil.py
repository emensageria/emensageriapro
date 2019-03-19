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
from emensageriapro.s2405.forms import *
from emensageriapro.s2405.models import *
from emensageriapro.controle_de_acesso.models import *
import json
import base64

#IMPORTACOES
@login_required
def apagar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2405_brasil_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2405_brasil')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    s2405_brasil = get_object_or_404(s2405brasil.objects.using( db_slug ), excluido = False, id = s2405_brasil_id)
    dados_evento = {}
    if s2405_brasil_id:
        dados_evento = s2405_brasil.evento()
        if dados_evento['status'] != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s2405_brasil_apagar'] = 0
            dict_permissoes['s2405_brasil_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == STATUS_EVENTO_CADASTRADO:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(s2405_brasil), indent=4, sort_keys=True, default=str)
            obj = s2405brasil.objects.using( db_slug ).get(id = s2405_brasil_id)
            obj.delete(request=request)
            #s2405_brasil_apagar_custom
            #s2405_brasil_apagar_custom
            messages.success(request, u'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             's2405_brasil', s2405_brasil_id, usuario_id, 3)
        else:
            messages.error(request, u'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 's2405_brasil_salvar':
            return redirect('s2405_brasil', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,

        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,

        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 's2405_brasil_apagar.html', context)

from rest_framework import generics
from rest_framework.permissions import IsAdminUser


class s2405brasilList(generics.ListCreateAPIView):
    db_slug = 'default'
    queryset = s2405brasil.objects.using(db_slug).all()
    serializer_class = s2405brasilSerializer
    # permission_classes = (IsAdminUser,)


class s2405brasilDetail(generics.RetrieveUpdateDestroyAPIView):
    db_slug = 'default'
    queryset = s2405brasil.objects.using(db_slug).all()
    serializer_class = s2405brasilSerializer
    # permission_classes = (IsAdminUser,)


def render_to_pdf(template_src, context_dict={}):
    from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


@login_required
def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #s2405_brasil_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2405_brasil')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos


    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_bairro': 0,
            'show_cep': 1,
            'show_codmunic': 1,
            'show_complemento': 0,
            'show_dsclograd': 1,
            'show_nrlograd': 1,
            'show_s2405_evtcdbenefalt': 1,
            'show_tplograd': 1,
            'show_uf': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'bairro__icontains': 'bairro__icontains',
                'cep__icontains': 'cep__icontains',
                'codmunic__icontains': 'codmunic__icontains',
                'complemento__icontains': 'complemento__icontains',
                'dsclograd__icontains': 'dsclograd__icontains',
                'nrlograd__icontains': 'nrlograd__icontains',
                's2405_evtcdbenefalt': 's2405_evtcdbenefalt',
                'tplograd__icontains': 'tplograd__icontains',
                'uf__icontains': 'uf__icontains',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'bairro__icontains': 'bairro__icontains',
                'cep__icontains': 'cep__icontains',
                'codmunic__icontains': 'codmunic__icontains',
                'complemento__icontains': 'complemento__icontains',
                'dsclograd__icontains': 'dsclograd__icontains',
                'nrlograd__icontains': 'nrlograd__icontains',
                's2405_evtcdbenefalt': 's2405_evtcdbenefalt',
                'tplograd__icontains': 'tplograd__icontains',
                'uf__icontains': 'uf__icontains',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        s2405_brasil_lista = s2405brasil.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(s2405_brasil_lista) > 100:
            filtrar = True
            s2405_brasil_lista = None
            messages.warning(request, u'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #s2405_brasil_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 's2405_brasil'
        context = {
            's2405_brasil_lista': s2405_brasil_lista,
  
            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,

        }
        if for_print in (0,1):
            return render(request, 's2405_brasil_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2405_brasil_listar.html',
                filename="s2405_brasil.pdf",
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
            response = render_to_response('s2405_brasil_listar.html', context)
            filename = "s2405_brasil.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/s2405_brasil_csv.html', context)
            filename = "s2405_brasil.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
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

@login_required
def salvar(request, hash):
    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO
    db_slug = 'default'
    try:
        usuario_id = request.user.id
        dict_hash = get_hash_url( hash )
        s2405_brasil_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='s2405_brasil')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if s2405_brasil_id:
        s2405_brasil = get_object_or_404(s2405brasil.objects.using( db_slug ), excluido = False, id = s2405_brasil_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = STATUS_EVENTO_CADASTRADO
    if s2405_brasil_id:
        dados_evento = s2405_brasil.evento()
        if dados_evento['status'] != STATUS_EVENTO_CADASTRADO:
            dict_permissoes['s2405_brasil_apagar'] = 0
            dict_permissoes['s2405_brasil_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if s2405_brasil_id:
            s2405_brasil_form = form_s2405_brasil(request.POST or None,
                                         instance = s2405_brasil,
                                         slug = db_slug,
                                         initial={'excluido': False})
        else:
            s2405_brasil_form = form_s2405_brasil(request.POST or None,
                                         slug = db_slug,
                                         initial={'excluido': False})
        if request.method == 'POST':
            if s2405_brasil_form.is_valid():

                dados = s2405_brasil_form.cleaned_data
                obj = s2405_brasil_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')

                if not s2405_brasil_id:
                    gravar_auditoria('{}',
                                 json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                 's2405_brasil', obj.id, usuario_id, 1)
                else:

                    gravar_auditoria(json.dumps(model_to_dict(s2405_brasil), indent=4, sort_keys=True, default=str),
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     's2405_brasil', s2405_brasil_id, usuario_id, 2)
                  
                if request.session['retorno_pagina'] not in ('s2405_brasil_apagar', 's2405_brasil_salvar', 's2405_brasil'):
                    return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                if s2405_brasil_id != obj.id:
                    url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                    return redirect('s2405_brasil_salvar', hash=url_hash)
            else:
                messages.error(request, u'Erro ao salvar!')
        s2405_brasil_form = disabled_form_fields(s2405_brasil_form, permissao.permite_editar)
        if s2405_brasil_id:
            if dados_evento['status'] != 0:
                s2405_brasil_form = disabled_form_fields(s2405_brasil_form, 0)
        #s2405_brasil_campos_multiple_passo3

        for field in s2405_brasil_form.fields.keys():
            s2405_brasil_form.fields[field].widget.attrs['ng-model'] = 's2405_brasil_'+field
        if int(dict_hash['print']):
            s2405_brasil_form = disabled_form_for_print(s2405_brasil_form)
        #[VARIAVEIS_SECUNDARIAS_VAZIAS]
        if s2405_brasil_id:
            s2405_brasil = get_object_or_404(s2405brasil.objects.using( db_slug ), excluido = False, id = s2405_brasil_id)
            pass
        else:
            s2405_brasil = None
        #s2405_brasil_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 's2405_brasil' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 's2405_brasil_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=s2405_brasil_id, tabela='s2405_brasil').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            's2405_brasil': s2405_brasil,
            's2405_brasil_form': s2405_brasil_form,
            'mensagem': mensagem,
            's2405_brasil_id': int(s2405_brasil_id),
            'usuario': usuario,
  
            'hash': hash,
            #[VARIAVEIS_SECUNDARIAS]
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,
  
            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #s2405_brasil_salvar_custom_variaveis_context#
        }
        if for_print in (0,1 ):
            return render(request, 's2405_brasil_salvar.html', context)
        elif for_print == 2:
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='s2405_brasil_salvar.html',
                filename="s2405_brasil.pdf",
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
            response = render_to_response('s2405_brasil_salvar.html', context)
            filename = "s2405_brasil.xls"
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

