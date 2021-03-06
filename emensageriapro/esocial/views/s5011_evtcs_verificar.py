#coding: utf-8
# © 2018 Marcelo Medeiros de Vasconcellos
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

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

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__credits__ = ["Marcelo Medeiros de Vasconcellos"]
__version__ = "1.0.0"
__maintainer__ = "Marcelo Medeiros de Vasconcellos"
__email__ = "marcelomdevasconcellos@gmail.com"


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.esocial.forms import *
from emensageriapro.esocial.models import *
from emensageriapro.controle_de_acesso.models import Usuarios
from emensageriapro.s5011.models import *
from emensageriapro.s5011.forms import *
from emensageriapro.functions import render_to_pdf, txt_xml
from wkhtmltopdf.views import PDFTemplateResponse
from datetime import datetime
import base64
import os


from emensageriapro.esocial.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


@login_required
def verificar(request, pk, output=None):

    if request.user.has_perm('esocial.can_see_s5011evtCS'):
    
        s5011_evtcs = get_object_or_404(s5011evtCS, id=pk)
        s5011_evtcs_lista = s5011evtCS.objects.filter(id=pk).all()

        
        s5011_infocpseg_lista = s5011infoCPSeg.objects.filter(s5011_evtcs_id__in = listar_ids(s5011_evtcs_lista) ).all()
        s5011_infopj_lista = s5011infoPJ.objects.filter(s5011_evtcs_id__in = listar_ids(s5011_evtcs_lista) ).all()
        s5011_infoatconc_lista = s5011infoAtConc.objects.filter(s5011_infopj_id__in = listar_ids(s5011_infopj_lista) ).all()
        s5011_ideestab_lista = s5011ideEstab.objects.filter(s5011_evtcs_id__in = listar_ids(s5011_evtcs_lista) ).all()
        s5011_infoestab_lista = s5011infoEstab.objects.filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).all()
        s5011_infocomplobra_lista = s5011infoComplObra.objects.filter(s5011_infoestab_id__in = listar_ids(s5011_infoestab_lista) ).all()
        s5011_idelotacao_lista = s5011ideLotacao.objects.filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).all()
        s5011_infotercsusp_lista = s5011infoTercSusp.objects.filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).all()
        s5011_infoemprparcial_lista = s5011infoEmprParcial.objects.filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).all()
        s5011_dadosopport_lista = s5011dadosOpPort.objects.filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).all()
        s5011_basesremun_lista = s5011basesRemun.objects.filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).all()
        s5011_basesavnport_lista = s5011basesAvNPort.objects.filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).all()
        s5011_infosubstpatropport_lista = s5011infoSubstPatrOpPort.objects.filter(s5011_idelotacao_id__in = listar_ids(s5011_idelotacao_lista) ).all()
        s5011_basesaquis_lista = s5011basesAquis.objects.filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).all()
        s5011_basescomerc_lista = s5011basesComerc.objects.filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).all()
        s5011_infocrestab_lista = s5011infoCREstab.objects.filter(s5011_ideestab_id__in = listar_ids(s5011_ideestab_lista) ).all()
        s5011_infocrcontrib_lista = s5011infoCRContrib.objects.filter(s5011_evtcs_id__in = listar_ids(s5011_evtcs_lista) ).all()

        request.session['return_pk'] = pk
        request.session['return_page'] = 's5011_evtcs'

        context = {
            's5011_evtcs_lista': s5011_evtcs_lista,
            'usuario': Usuarios.objects.get(user_id=request.user.id),
            'pk': pk,
            's5011_evtcs': s5011_evtcs,
            's5011_infocpseg_lista': s5011_infocpseg_lista,
            's5011_infopj_lista': s5011_infopj_lista,
            's5011_infoatconc_lista': s5011_infoatconc_lista,
            's5011_ideestab_lista': s5011_ideestab_lista,
            's5011_infoestab_lista': s5011_infoestab_lista,
            's5011_infocomplobra_lista': s5011_infocomplobra_lista,
            's5011_idelotacao_lista': s5011_idelotacao_lista,
            's5011_infotercsusp_lista': s5011_infotercsusp_lista,
            's5011_infoemprparcial_lista': s5011_infoemprparcial_lista,
            's5011_dadosopport_lista': s5011_dadosopport_lista,
            's5011_basesremun_lista': s5011_basesremun_lista,
            's5011_basesavnport_lista': s5011_basesavnport_lista,
            's5011_infosubstpatropport_lista': s5011_infosubstpatropport_lista,
            's5011_basesaquis_lista': s5011_basesaquis_lista,
            's5011_basescomerc_lista': s5011_basescomerc_lista,
            's5011_infocrestab_lista': s5011_infocrestab_lista,
            's5011_infocrcontrib_lista': s5011_infocrcontrib_lista,
            'modulos': ['esocial', ],
            'paginas': ['s5011_evtcs', ],
            'data': datetime.now(),
            'output': output,
        }
        
        if output == 'pdf':
        
            response = PDFTemplateResponse(
                request=request,
                template='s5011_evtcs_verificar.html',
                filename="s5011_evtcs.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 20,
                             'zoom': 1,
                             'viewport-size': '1366 x 513',
                             'javascript-delay': 1000,
                             'footer-center': u'Página [page]/[topage]',
                             'footer-font-size': 10,
                             'no-stop-slow-scripts': True})
                            
            return response

        elif output == 'xls':
        
            response = render_to_response('s5011_evtcs_verificar.html', context)
            filename = "%s.xls" % s5011_evtcs.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            
            return response

        elif output == 'csv':
        
            response = render_to_response('s5011_evtcs_verificar.html', context)
            filename = "%s.csv" % s5011_evtcs.identidade
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response

        else:
        
            return render(request, 's5011_evtcs_verificar.html', context)

    else:

        context = {
            'modulos': ['esocial', ],
            'paginas': ['s5011_evtcs', ],
            'data': datetime.now(),
        }

        return render(request, 'permissao_negada.html', context)