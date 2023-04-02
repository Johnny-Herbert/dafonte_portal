from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.utils.translation import ugettext as _

from portal.models import Opportunity, PracticeArea, SpecializationSector
from portal.views import PageView, View
from .models import (
    Application,
    ApplicationLanguage,
    Academic,
    ProfessionalExperience
)

from .forms import (
    AcademicForm,
    ApplicationForm,
    ApplicationLanguageForm,
    ProfessionalExperienceForm
)


class OpportunityView(PageView):
    template_name = "opportunity.html"
    slug = "opportunity"
    has_errors = False
    Opportunity_id = None
    Opportunity_active = None

    @transaction.atomic
    def _validate_formset(self, model_class, form_class, prefix, application):
        Formset = modelformset_factory(model_class, form=form_class)
        formset = Formset(self.request.POST, prefix=prefix)
        if not formset.is_valid():
            self.has_errors = True
        return formset

    @transaction.atomic
    def _save_formset(self, formset, model_class, created_application):
        instances = formset.cleaned_data
        for fields in instances:
            if fields:
                if fields.get('incomplete_course'):
                    fields['period'] = ''
                    fields['shift'] = ''
                if not fields.get('language') and fields.get('level'):
                    # se nao for definido um idioma, ignore-o
                    continue
                new_instance = model_class(**fields)
                new_instance.application = created_application
                new_instance.save()

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        super(OpportunityView, self).get(request, *args, **kwargs)
        context = super().get_context_data(**kwargs)
        created_application = None

        application_form = ApplicationForm(request.POST, prefix='personal')

        if not application_form.is_valid():
            self.has_errors = True
        academics = self._validate_formset(Academic, AcademicForm, "academic", created_application)
        professionals = self._validate_formset(ProfessionalExperience, ProfessionalExperienceForm, "professional", created_application )
        languages = self._validate_formset(ApplicationLanguage, ApplicationLanguageForm, "language", created_application )

        opportunity = None
        if self.opportunity_id:
            opportunity = Opportunity.objects.filter(id=self.opportunity_id).first()
            context['opportunity'] = opportunity

        if self.has_errors:
            context['application'] = application_form
            context['academics'] = academics
            context['professionals'] = professionals
            context['languages'] = languages
            context['flash'] = {'status': 'error', 'message': _('Verifique se todos os campos foram preenchidos corretamente')}
        else:
            created_application = application_form.save(commit=False)
            if self.opportunity_id and self.opportunity_active:
                created_application.opportunity_id = self.opportunity_id
                if opportunity.role:
                    created_application.role = opportunity.role.role_type
                else:
                    # workaround para adicionar o role definido em
                    # Application.ROLES_CHOICES ao curriculo pelo nome da vaga
                    # para as oportunidades antigas
                    title = opportunity.title.lower()
                    if 'advogad' in title:
                        role = 'LAWYER'
                    elif 'estagiari' in title or 'estagiári' in title:
                        role = 'INTERN'
                    else:
                        role = 'SUPPORT'
                    created_application.role = role
            created_application.save()
            self._save_formset(academics, Academic, created_application)
            self._save_formset(professionals, ProfessionalExperience, created_application)
            self._save_formset(languages, ApplicationLanguage, created_application)
            context['flash'] = {'status': 'success', 'message': _('Formulário enviado com sucesso!')}
        context['role_choices'] = Application.ROLE_CHOICES
        context['local_choices'] = Application.LOCAL_CHOICES
        context['period_choices'] = Academic.PERIOD_CHOICES
        context['shift_choices'] = Academic.SHIFT_CHOICES
        context['language_level_choices'] = ApplicationLanguage.LEVEL_CHOICES
        context['practice_areas'] = PracticeArea.objects.all()
        context['specialization_sectors'] = SpecializationSector.objects.all()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.opportunity_id = self.kwargs.get("opportunity_id", None)
        self.opportunity_active = self.kwargs.get("opportunity_active", None)
        if self.opportunity_id is not None:
            opportunity = get_object_or_404(Opportunity, id=self.opportunity_id)
            context['opportunity'] = opportunity
            self.opportunity_active = opportunity.active
            if not opportunity.active:
                context['role_choices'] = Application.ROLE_CHOICES
                context['local_choices'] = Application.LOCAL_CHOICES
        else:
            context['role_choices'] = Application.ROLE_CHOICES
            context['local_choices'] = Application.LOCAL_CHOICES
        context['period_choices'] = Academic.PERIOD_CHOICES
        context['shift_choices'] = Academic.SHIFT_CHOICES
        context['language_level_choices'] = ApplicationLanguage.LEVEL_CHOICES
        context['practice_areas'] = PracticeArea.objects.all()
        context['specialization_sectors'] = SpecializationSector.objects.all()
        return context



from io import BytesIO
from django.core.files import File
from .utils import generate_obj_pdf
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class ApplyToPdf(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        apply_id = self.kwargs.get("apply_id", None)
        return generate_obj_pdf(apply_id)
