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
from emensageriapro.s1200.forms import *
from emensageriapro.s1200.models import *
from emensageriapro.controle_de_acesso.models import *



@login_required
def salvar(request, pk=None, tab='master', output=None):

    from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO

    evento_dados = {}
    evento_dados['status'] = STATUS_EVENTO_CADASTRADO

    if pk:

        s1200_infoperant_infotrabinterm = get_object_or_404(s1200infoPerAntinfoTrabInterm, id=pk)
        evento_dados = s1200_infoperant_infotrabinterm.evento()

    if request.user.has_perm('s1200.can_see_s1200infoPerAntinfoTrabInterm'):

        if pk:

            s1200_infoperant_infotrabinterm_form = form_s1200_infoperant_infotrabinterm(
                request.POST or None,
                instance=s1200_infoperant_infotrabinterm)
                     
        else:

            s1200_infoperant_infotrabinterm_form = form_s1200_infoperant_infotrabinterm(request.POST or None)
                     
        if request.method == 'POST':

            if s1200_infoperant_infotrabinterm_form.is_valid():

                obj = s1200_infoperant_infotrabinterm_form.save(request=request)
                messages.success(request, u'Salvo com sucesso!')
                 
                if 's1200-infoperant-infotrabinterm' not in request.session['return']:

                    return HttpResponseRedirect(request.session['return'])

                if pk != obj.id:

                    return redirect(
                        's1200_infoperant_infotrabinterm_salvar',
                        pk=obj.id)

            else:

                messages.error(request, u'Erro ao salvar!')

        s1200_infoperant_infotrabinterm_form = disabled_form_fields(
            s1200_infoperant_infotrabinterm_form,
            request.user.has_perm('s1200.change_s1200infoPerAntinfoTrabInterm'))

        if pk:

            if evento_dados['status'] != STATUS_EVENTO_CADASTRADO:

                s1200_infoperant_infotrabinterm_form = disabled_form_fields(s1200_infoperant_infotrabinterm_form, 0)

        if output:

            s1200_infoperant_infotrabinterm_form = disabled_form_for_print(s1200_infoperant_infotrabinterm_form)



        if pk:

            s1200_infoperant_infotrabinterm = get_object_or_404(s1200infoPerAntinfoTrabInterm, id=pk)


        else:

            s1200_infoperant_infotrabinterm = None

        tabelas_secundarias = []

        #if tab or 's1200_infoperant_infotrabinterm' in request.session['return_page']:
        #
        #    request.session['return_pk'] = pk
        #    request.session['return_tab'] = tab
        #    request.session['return_page'] = 's1200_infoperant_infotrabinterm_salvar'

        controle_alteracoes = Auditoria.objects.filter(identidade=pk, tabela='s1200_infoperant_infotrabinterm').all()

        if not request.POST:
            request.session['return'] = request.META.get('HTTP_REFERER')

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'evento_dados': evento_dados,
            'controle_alteracoes': controle_alteracoes,
            's1200_infoperant_infotrabinterm': s1200_infoperant_infotrabinterm,
            's1200_infoperant_infotrabinterm_form': s1200_infoperant_infotrabinterm_form,
            'modulos': ['s1200', ],
            'paginas': ['s1200_infoperant_infotrabinterm', ],
            'data': datetime.datetime.now(),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': tab,
            #s1200_infoperant_infotrabinterm_salvar_custom_variaveis_context#
        }

        if output == 'pdf':

            from wkhtmltopdf.views import PDFTemplateResponse

            response = PDFTemplateResponse(
                request=request,
                template='s1200_infoperant_infotrabinterm_salvar.html',
                filename="s1200_infoperant_infotrabinterm.pdf",
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
                             "no-stop-slow-scripts": True}, )

            return response

        elif output == 'xls':

            from django.shortcuts import render_to_response

            response = render_to_response('s1200_infoperant_infotrabinterm_salvar.html', context)
            filename = "s1200_infoperant_infotrabinterm.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'

            return response

        else:

            return render(request, 's1200_infoperant_infotrabinterm_salvar.html', context)

    else:

        context = {
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            'output': output,
            'tab': tab,
            'modulos': ['s1200', ],
            'paginas': ['s1200_infoperant_infotrabinterm', ],
            'data': datetime.datetime.now(),
        }

        return render(request,
                      'permissao_negada.html',
                      context)