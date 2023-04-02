from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.db import models
from django.contrib.admin import StackedInline, register
from modeltranslation.admin import TabbedTranslationAdmin


from applying.models import (
    Application, ProfessionalExperience, Academic, ApplicationLanguage
)
from portal.models import Opportunity, PracticeArea, SpecializationSector
from applying.actions import print_cv_selected


class ProfessionalExperienceInline(admin.StackedInline):
    id = models.AutoField(primary_key=True, editable=False)
    model = ProfessionalExperience
    # readonly_fields = (
    #     "enterprise", "function", "area", "periodo", "activities",
    #     "application"
    # )
    extra = 0


class AcademicInline(admin.TabularInline):
    id = models.AutoField(primary_key=True, editable=False)
    model = Academic
    # readonly_fields = ("course", "institution", "conclusion", "application")
    extra = 0


class ApplicationLanguageInline(admin.TabularInline):
    id = models.AutoField(primary_key=True, editable=False)
    model = ApplicationLanguage
    # readonly_fields = ("language",)
    extra = 0


class RoleListFilter(admin.SimpleListFilter):
    title = 'Cargo'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'role'

    default_value = None

    def lookups(self, request, model_admin):
        return sorted(Application.ROLE_CHOICES, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(role=self.value())
        return queryset


class LocalListFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Local'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'local'

    default_value = None

    def lookups(self, request, model_admin):
        return sorted(Application.LOCAL_CHOICES, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(local=self.value())
        return queryset


class OpportunityListFilter(admin.SimpleListFilter):

    """
    This filter will always return a subset of the instances in a Model,
    either filtering by the user choice or by a default value.
    """
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Vagas'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'opportunities'

    default_value = None

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        list_of_opportunities = []
        queryset = Opportunity.objects.all()
        for opportunity in queryset:
            list_of_opportunities.append(
                (str(opportunity.id), opportunity.title)
            )
        return sorted(list_of_opportunities, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(opportunity_id=self.value())
        return queryset


class PracticeAreaListFilter(admin.SimpleListFilter):
    title = 'Área de atuação'
    parameter_name = 'practice_areas'
    default_value = None

    def lookups(self, request, model_admin):
        data = []
        queryset = PracticeArea.objects.all()
        for instance in queryset:
            data.append(
                (str(instance.id), instance.name)
            )
        return sorted(data, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(practice_areas=self.value())
        return queryset


class SpecializationSectorListFilter(admin.SimpleListFilter):
    title = 'Setor de especialização'
    parameter_name = 'specialization_sectors'
    default_value = None

    def lookups(self, request, model_admin):
        data = []
        queryset = SpecializationSector.objects.all()
        for instance in queryset:
            data.append(
                (str(instance.id), instance.name)
            )
        return sorted(data, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(specialization_sectors=self.value())
        return queryset


# Register your models here.
@register(Application)
class ApplicationAdmin(TabbedTranslationAdmin):
    list_display = [
        "name", "email", "created_at", "opportunity", "role", "intend_area",
        "practice_areas", "specialization_sectors",
        "apply_actions", "is_downloaded"
    ]
    fields = [
        "name", "email", "phone", "address", "created_at", "role",
        "intend_area", "local", "practice_areas", "specialization_sectors",
        "opportunity", "extra_qualification"
    ]
    inlines = [
        ProfessionalExperienceInline, AcademicInline, ApplicationLanguageInline
    ]
    search_fields = (
        "name", "opportunity__title", "role", "local"
    )
    list_filter = (
        OpportunityListFilter, RoleListFilter, LocalListFilter,
        PracticeAreaListFilter, SpecializationSectorListFilter,
        ('is_downloaded', admin.BooleanFieldListFilter),
    )
    actions = [print_cv_selected]

    def has_delete_permission(self, request, obj=None):
        # ignora action para remover objetos selecionados
        # para evitar miss click ao imprimir curriculos
        return False

    def apply_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Imprimir</a>&nbsp;',
            reverse('apply-pdf', args=[obj.id]),
        )
    apply_actions.short_description = 'Currículo'
    apply_actions.allow_tags = True


# @register(ProfessionalExperience)
class ProfessionalExperienceAdmin(TabbedTranslationAdmin):
    list_display = [
        "enterprise", "function", "area", "date_begin", "date_finish",
        "activities", "application"
    ]


# @register(Academic)
class AcademicAdmin(TabbedTranslationAdmin):
    list_display = ["course", "institution", "conclusion", "application"]


# @register(ApplicationLanguage)
class ApplicationLanguageAdmin(TabbedTranslationAdmin):
    list_display = ["language"]
