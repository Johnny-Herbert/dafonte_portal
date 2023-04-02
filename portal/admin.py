from django.utils import timezone
from django.contrib import admin
from django.contrib.admin import StackedInline, register, TabularInline
from django.core.exceptions import ValidationError
from django.forms import ModelForm, BaseInlineFormSet
from modeltranslation.admin import (
    TabbedTranslationAdmin, TranslationTabularInline,
    TranslationStackedInline
)

from portal.models import (
    PracticeArea, Approach, ApproachSector, Language, Award, PageParameter,
    Page, Partner, Affiliate, Office, SiteParameter, Publication, Event,
    Opportunity, OpportunityRole, SpecializationSector, SocialEntity,
    Contact, Values
)

from portal.forms import OpportunityRoleForm


class MemberLawyerPracticeAreaInLine(TabularInline):
    model = PracticeArea.lawyers.through
    extra = 0
    verbose_name = 'advogado'
    verbose_name_plural = 'advogados'


class PageParameterInline(TranslationTabularInline):
    model = PageParameter
    extra = 0


@register(Page)
class PageAdmin(TabbedTranslationAdmin):
    prepopulated_fields = dict(slug=["title"])
    inlines = [PageParameterInline]


class ApproachInline(TranslationTabularInline):
    model = Approach
    extra = 0


class ApproachSectorInline(TranslationTabularInline):
    model = ApproachSector
    extra = 0


@register(PracticeArea)
class PracticeAreaAdmin(TabbedTranslationAdmin):
    list_display = ["name", "description"]
    fieldsets = [
        (None, dict(fields=["name", "description"])),
        ("Arquivos", dict(fields=["picture"]))
    ]
    inlines = [MemberLawyerPracticeAreaInLine, ApproachInline]


@register(SpecializationSector)
class SpecializationSectorAdmin(TabbedTranslationAdmin):
    list_display = ["name", "description"]
    fieldsets = [
        (None, dict(fields=["name", "description"])),
        ("Arquivos", dict(fields=["picture"]))
    ]
    inlines = [ApproachSectorInline]


@register(Publication)
class PublicationAdmin(TabbedTranslationAdmin):
    list_display = ["__str__", "description_short", "creation_date"]
    filter_horizontal = ["related_members"]


@register(Event)
class EventAdmin(TabbedTranslationAdmin):
    list_display = ["description_short", "date", "time"]


@register(Award)
class AwardAdmin(TabbedTranslationAdmin):
    list_display = ["title", "is_highlight"]


@register(Contact)
class ContactAdmin(TabbedTranslationAdmin):
    list_display = ["name", "email", "telefone", "entrou_em_contato_em"]
    fieldsets = [
        (None, dict(fields=["name", "email", "telefone", "message"]))
    ]

    def entrou_em_contato_em(self, obj):
        return timezone.localtime(obj.created_at)


@register(Office)
class OfficeAdmin(TabbedTranslationAdmin):
    list_display = ["city", "is_parent", "address", "email", "office_order"]
    ordering = ["-is_parent", "office_order"]


@register(OpportunityRole)
class OpportunityRoleAdmin(admin.ModelAdmin):
    form = OpportunityRoleForm
    list_display = ["name"]
    model = OpportunityRole

    def get_readonly_fields(self, request, obj=None):
        """ ignora campos que nao podem ser editáveis """
        readonly_fields = ['role_type']
        if obj and obj.role_type in ['LAWYER', 'INTERN', 'TRAINEE']:
            readonly_fields = ['name', 'role_type']
        return readonly_fields


@register(Opportunity)
class OpportunityAdmin(TabbedTranslationAdmin):
    list_display = ["title", "role", "spots", "active"]


# Models que não têm tradução
admin.site.register([Partner, Affiliate])
# Models que têm tradução
admin.site.register(
    [
        SiteParameter, Language, SocialEntity, Values,
        ApproachSector
    ], TabbedTranslationAdmin
)
