from django.contrib import admin
from django.forms import ModelForm, BaseInlineFormSet, ValidationError
from django.db import models
 
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from members.models import JobTitle, Member, MemberAdministrativeStaff, MemberIntern, MemberLawyer, MemberTrainee, MemberType, AwardMembers
from members.proxies import ProxyIntern, ProxyLawyer, ProxyTrainee, ProxyAdministrativeStaff


class BaseMemberChildInlineFormSet(BaseInlineFormSet):

    def clean(self):
        super().clean()

        if len(self.forms[0].cleaned_data) == 0:
            raise ValidationError("Dados de {} não preenchidos.".format(self.model._meta.verbose_name))

class AwardMembersInline(admin.StackedInline):
    id = models.AutoField(primary_key=True, editable=False)
    model = AwardMembers
    fk_name = 'member'
    extra = 0

class MemberLawyerInline(TranslationStackedInline):
    model = MemberLawyer
    formset = BaseMemberChildInlineFormSet
    classes = ["collapse"]
    filter_horizontal = ["practice_areas", "languages", "specialization_sector", "awards"]


class MemberAdministrativeStaffInline(admin.StackedInline):
    model = MemberAdministrativeStaff
    formset = BaseMemberChildInlineFormSet
    classes = ["collapse"]


class MemberTraineeInline(admin.StackedInline):
    model = MemberTrainee
    formset = BaseMemberChildInlineFormSet
    classes = ["collapse"]
    filter_horizontal = ["practice_areas", "specialization_sectors"]


class MemberInternInline(admin.StackedInline):
    model = MemberIntern
    formset = BaseMemberChildInlineFormSet
    classes = ["collapse"]
    filter_horizontal = ["practice_areas", "specialization_sectors"]


class BaseMemberAdmin(TabbedTranslationAdmin):
    exclude = ("type", )
    readonly_fields = ("member_type", )
    search_fields = ["first_name", "last_name"]

    def member_type(self, obj):
        return MemberType.objects.get(pk=self.model.member_type)
    member_type.short_description = "Tipo de Membro"

    def save_model(self, request, obj, form, change):
        if not change:
            obj.type_id = self.model.member_type
        return super().save_model(request, obj, form, change)

@admin.register(ProxyIntern)
class ProxyInternAdmin(BaseMemberAdmin):
    inlines = [MemberInternInline]


@admin.register(ProxyLawyer)
class ProxyLawyerAdmin(BaseMemberAdmin):
    inlines = [MemberLawyerInline]


@admin.register(ProxyTrainee)
class ProxyTraineeAdmin(BaseMemberAdmin):
    inlines = [MemberTraineeInline]


@admin.register(ProxyAdministrativeStaff)
class ProxyAdministrativeStaffAdmin(BaseMemberAdmin):
    inlines = [MemberAdministrativeStaffInline]

admin.site.register(AwardMembers)
admin.site.register(JobTitle, TabbedTranslationAdmin)
