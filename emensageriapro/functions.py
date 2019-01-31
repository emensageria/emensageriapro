#coding: utf-8
import datetime


"""

    eMensageriaPro - Sistema de Gerenciamento de Eventos do eSocial e EFD-Reinf <www.emensageria.com.br>
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



def txt_xml(texto):

    texto = str(texto)
    texto = texto.replace(">",'&gt;')
    texto = texto.replace("<",'&lt;')
    texto = texto.replace("&",'&amp;')
    texto = texto.replace('"','&quot;')
    texto = texto.replace("'",'&apos;')

    return texto



def identidade_evento(obj):
    from emensageriapro.mensageiro.models import TransmissorEventosEsocial

    identidade = 'ID'
    identidade += str(obj.tpinsc)
    nr_insc = obj.nrinsc

    while len(nr_insc) != 14:
        nr_insc = nr_insc+'0'

    identidade += nr_insc
    identidade += str(obj.criado_em.year)
    mes = str(obj.criado_em.month)

    if len(mes) == 1:
        mes = '0'+mes

    identidade += mes
    dia = str(obj.criado_em.day)

    if len(dia) == 1:
        dia = '0'+dia

    identidade += dia
    hora = str(obj.criado_em.hour)

    if len(hora) == 1:
        hora = '0'+hora

    identidade += hora
    minuto = str(obj.criado_em.minute)

    if len(minuto) == 1:
        minuto = '0'+minuto

    identidade += minuto
    segundo = str(obj.criado_em.second)

    if len(segundo) == 1:
        segundo = '0'+segundo

    identidade += segundo
    existe = True
    n = 0

    while existe:

        n+=1
        sequencial = str(n)

        while len(sequencial) != 5:
            sequencial = '0'+sequencial

        identidade_temp = identidade + sequencial

        lista_eventos = TransmissorEventosEsocial.objects.\
            filter(criado_em=obj.criado_em,
                   excluido=False,
                   identidade = identidade_temp).all()

        if not lista_eventos:
            obj.identidade=identidade_temp
            obj.save()
            existe = False

    return identidade_temp


def get_xmlns(arquivo):
    from emensageriapro.padrao import ler_arquivo

    texto = ler_arquivo( arquivo )
    b = texto.split('xmlns="')
    c = b[1].split('"')
    return c[0]
