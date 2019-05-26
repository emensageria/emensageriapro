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
from emensageriapro.efdreinf.forms import *
from emensageriapro.efdreinf.models import *
from emensageriapro.controle_de_acesso.models import Usuarios, ConfigPermissoes, ConfigPerfis, ConfigModulos, ConfigPaginas
from emensageriapro.r2050.models import *
from emensageriapro.r2050.forms import *
from emensageriapro.functions import render_to_pdf, txt_xml
from wkhtmltopdf.views import PDFTemplateResponse
from datetime import datetime
import base64
import os


from emensageriapro.efdreinf.models import STATUS_EVENTO_CADASTRADO, STATUS_EVENTO_IMPORTADO, \
    STATUS_EVENTO_DUPLICADO, STATUS_EVENTO_GERADO, \
    STATUS_EVENTO_GERADO_ERRO, STATUS_EVENTO_ASSINADO, \
    STATUS_EVENTO_ASSINADO_ERRO, STATUS_EVENTO_VALIDADO, \
    STATUS_EVENTO_VALIDADO_ERRO, STATUS_EVENTO_AGUARD_PRECEDENCIA, \
    STATUS_EVENTO_AGUARD_ENVIO, STATUS_EVENTO_ENVIADO, \
    STATUS_EVENTO_ENVIADO_ERRO, STATUS_EVENTO_PROCESSADO


def gerar_xml_r2050(request, r2050_evtcomprod_id, versao=None):

    from django.template.loader import get_template
    from emensageriapro.functions import get_xmlns

    if r2050_evtcomprod_id:

        r2050_evtcomprod = get_object_or_404(
            r2050evtComProd,
            excluido = False,
            id = r2050_evtcomprod_id)

        if not versao or versao == '|':
            versao = r2050_evtcomprod.versao

        evento = 'r2050evtComProd'[5:]
        arquivo = 'xsd/efdreinf/%s/%s.xsd' % (versao, evento)

        import os.path

        if os.path.isfile(arquivo):

            xmlns = get_xmlns(arquivo)

        else:
        
            from django.contrib import messages

            messages.warning(request, '''
                Não foi capturar o XMLNS pois o XSD do 
                evento não está contido na pasta!''')

            xmlns = ''

        r2050_evtcomprod_lista = r2050evtComProd.objects. \
            filter(id=r2050_evtcomprod_id, excluido = False).all()
        
        r2050_tipocom_lista = r2050tipoCom.objects. \
            filter(r2050_evtcomprod_id__in=listar_ids(r2050_evtcomprod_lista)).all()
        
        r2050_infoproc_lista = r2050infoProc.objects. \
            filter(r2050_tipocom_id__in=listar_ids(r2050_tipocom_lista)).all()
        

        context = {
            'xmlns': xmlns,
            'versao': versao,
            'base': r2050_evtcomprod,
            'r2050_evtcomprod_lista': r2050_evtcomprod_lista,
            'r2050_evtcomprod_id': int(r2050_evtcomprod_id),
            'r2050_evtcomprod': r2050_evtcomprod,

            
            'r2050_tipocom_lista': r2050_tipocom_lista,
            'r2050_infoproc_lista': r2050_infoproc_lista,
        }

        t = get_template('r2050_evtcomprod.xml')
        xml = t.render(context)
        return xml




def gerar_xml_assinado(request, r2050_evtcomprod_id):

    from emensageriapro.settings import BASE_DIR
    from emensageriapro.mensageiro.functions.funcoes_efdreinf import salvar_arquivo_efdreinf
    from emensageriapro.mensageiro.functions.funcoes_efdreinf import assinar_efdreinf

    r2050_evtcomprod = get_object_or_404(
        r2050evtComProd,
        id=r2050_evtcomprod_id)

    if r2050_evtcomprod.arquivo_original:
    
        xml = ler_arquivo(r2050_evtcomprod.arquivo)

    else:
        xml = gerar_xml_r2050(request, r2050_evtcomprod_id)

    if 'Signature' in xml:
    
        xml_assinado = xml

    else:

        if not r2050_evtcomprod.transmissor_lote_efdreinf:

            from emensageriapro.mapa_processamento.views.funcoes_automaticas_efdreinf \
                import vincular_transmissor_efdreinf, criar_transmissor_efdreinf, get_grupo

            grupo = get_grupo(r2050evtComProd)

            criar_transmissor_efdreinf(request,
                                      grupo,
                                      r2050_evtcomprod.nrinsc,
                                      r2050_evtcomprod.tpinsc)

            vincular_transmissor_efdreinf(request,
                                         grupo,
                                         r2050evtComProd,
                                         r2050_evtcomprod)
        
        r2050_evtcomprod = get_object_or_404(
            r2050evtComProd,
            id=r2050_evtcomprod_id)
        
        xml_assinado = assinar_efdreinf(request, xml, r2050_evtcomprod.transmissor_lote_efdreinf_id)
        
    if r2050_evtcomprod.status in (
        STATUS_EVENTO_CADASTRADO,
        STATUS_EVENTO_IMPORTADO,
        STATUS_EVENTO_DUPLICADO,
        STATUS_EVENTO_GERADO):

        r2050evtComProd.objects.\
            filter(id=r2050_evtcomprod_id).update(status=STATUS_EVENTO_ASSINADO)

    arquivo = 'arquivos/Eventos/r2050_evtcomprod/%s.xml' % (r2050_evtcomprod.identidade)
    os.system('mkdir -p %s/arquivos/Eventos/r2050_evtcomprod/' % BASE_DIR)

    if not os.path.exists(BASE_DIR+arquivo):
        salvar_arquivo_efdreinf(arquivo, xml_assinado, 1)

    xml_assinado = ler_arquivo(arquivo)
    return xml_assinado



@login_required
def gerar_xml(request, hash):

    dict_hash = get_hash_url( hash )
    r2050_evtcomprod_id = int(dict_hash['id'])

    if r2050_evtcomprod_id:

        xml_assinado = gerar_xml_assinado(request, r2050_evtcomprod_id)
        return HttpResponse(xml_assinado, content_type='text/xml')

    context = {'data': datetime.now(),}
    return render(request, 'permissao_negada.html', context)