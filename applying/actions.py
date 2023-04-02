from applying.utils import (
    generate_obj_pdf, render_to_zip
)


def print_cv_selected(modeladmin, request, queryset):
    """
    django action para realizar o download de vários currículos de uma
    vez em formato zip
    """
    data = []
    for instance in queryset:
        pdf = generate_obj_pdf(instance.id, in_bytes=True)
        data.append(pdf)

    zip_response = render_to_zip(data)
    return zip_response


print_cv_selected.short_description = 'Imprimir currículos selecionados'
