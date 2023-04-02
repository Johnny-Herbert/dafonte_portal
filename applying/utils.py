from zipfile import ZipFile, ZIP_DEFLATED
from io import BytesIO, TextIOWrapper
from django.http import HttpResponse
from django.template.loader import get_template
from django.utils import timezone
from applying.models import (
    Application, ProfessionalExperience, Academic, ApplicationLanguage
)

from xhtml2pdf import pisa

REPLACE_CHARS = [
    ('–', '-')
]


def clean_context(context):
    new_context = {
        'apply': {},
    }
    apply = context['apply']

    # new_context['apply']['name'] = clean(apply.name)
    new_context['apply'] = {
        'name': clean(apply.name),
        'email': clean(apply.email),
        'address': clean(apply.address),
        'created_at': apply.created_at,
        'phone': apply.phone,
        'role': apply.get_role_display(),
        'raw_role': apply.role,
        'intend_area': clean(apply.intend_area),
        'extra_qualification': clean(apply.extra_qualification),
        'local': clean(apply.local)
    }
    professionals = []
    for obj in context['professionals']:
        clean_professional = {
            'enterprise': clean(obj.enterprise),
            'function': clean(obj.function),
            'actual_function': clean(obj.actual_function),
            'area': clean(obj.area),
            'activities': clean(obj.activities),
            'date_begin': obj.date_begin,
            'date_finish': obj.date_finish,
        }
        professionals.append(clean_professional)

    academics = []
    for obj in context['academics']:
        clean_academic = {
            'course': clean(obj.course),
            'institution': clean(obj.institution),
            'conclusion': obj.conclusion,
            'incomplete_course': obj.incomplete_course,
            'in_progress': obj.in_progress,
            'period': obj.period,
            'shift': obj.shift,
        }
        academics.append(clean_academic)

    languages = []
    for obj in context['languages']:
        clean_language = {
            'language': clean(obj.language).title(),
            'level': clean(obj.level)
        }
        languages.append(clean_language)

    opportunity = None
    if apply.opportunity:
        opportunity = {}
        opportunity['title'] = apply.opportunity.title
        opportunity['city'] = apply.opportunity.get_city_display

    new_context['professionals'] = professionals
    new_context['opportunity'] = opportunity
    new_context['academics'] = academics
    new_context['languages'] = languages
    new_context['specialization_sector'] = context['specialization_sector']
    new_context['practice_area'] = context['practice_area']

    return new_context


def clean(data):
    clean_data = data
    for (old, new) in REPLACE_CHARS:
        if type(clean_data) == str:
            clean_data = clean_data.replace(old, new)
    return clean_data


def render_to_pdf(template_src, context_dict={},
                  filename='dafonte_portal.pdf', in_bytes=False):
    template = get_template(template_src)
    cleaned_context = clean_context(context_dict)
    html = template.render(cleaned_context)
    result = BytesIO()
    try:
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    except:
        bytesHTML = BytesIO(html.encode("UTF-8"))
        bytesHTML = TextIOWrapper(bytesHTML, encoding='utf-8')
        pdf = pisa.pisaDocument(bytesHTML, result)

    if not pdf.err:
        pdf = result.getvalue()

        if in_bytes:
            return (filename, pdf)

        response = HttpResponse(pdf,
                                content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename={}'.format(
            filename
        )
        return response
    return None


def generate_obj_pdf(instance_id, in_bytes=False):
    obj = Application.objects.get(id=instance_id)

    # ao mudar o context mudar tambem na funcao que limpa os caracteres desconhecidos
    # /applying/utils.py
    # def clean_context(context):
    context = {
        'apply': obj,
        'opportunity': obj.opportunity,
        'practice_area': obj.practice_areas,
        'specialization_sector': obj.specialization_sectors,
        'professionals': ProfessionalExperience.objects.filter(
            application__id=instance_id
        ),
        'academics': Academic.objects.filter(application__id=instance_id),
        'languages': ApplicationLanguage.objects.filter(
            application__id=instance_id
        ),
        }
    filename = "Currículo-{}.pdf".format(obj.name)
    template = 'pdf/opportunity.html'
    if in_bytes:
        pdf = render_to_pdf(template, context, filename, in_bytes=True)
    else:
        pdf = render_to_pdf(template, context, filename)

    # atualiza o atributo que identifica se o curriculo foi visualizado/baixado
    obj.change_download_ok()

    return pdf


def render_to_zip(data):
    """
    retorna o response contendo o zip gerado com os curriculos selecionados
    @param data: tuple contendo o nome do arquivo e o pdf gerado em bytes
    """
    now = timezone.localtime(timezone.now()).strftime('%d-%m-%Y_%H:%M:%S')
    zip_filename = f'curriculos-{now}.zip'

    mem_zip = BytesIO()
    with ZipFile(mem_zip, mode="w", compression=ZIP_DEFLATED) as buffer:
        for pdf_data in data:
            name, pdf_byte = pdf_data[0], pdf_data[1]
            buffer.writestr(name, pdf_byte)
    zip_file = mem_zip.getvalue()

    response = HttpResponse(zip_file, content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename={zip_filename}'

    return response
