from modeltranslation.decorators import register
from modeltranslation.translator import translator, TranslationOptions

from members.models import JobTitle, Member, MemberLawyer, MemberType
from members.proxies import ProxyIntern, ProxyLawyer, ProxyTrainee, ProxyAdministrativeStaff


@register(JobTitle)
class JobTitleTranslation(TranslationOptions):
    fields = ["name"]


@register(MemberType)
class MemberTypeTranslation(TranslationOptions):
    fields = ["name"]


@register(MemberLawyer)
class MemberLawyerTranslation(TranslationOptions):
    fields = ["academic_formation", "professional_experience", "awards_and_publications", "other_activities"]


translator.register(Member)
translator.register([ProxyIntern, ProxyLawyer, ProxyTrainee, ProxyAdministrativeStaff])
