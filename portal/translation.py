from modeltranslation.decorators import register
from modeltranslation.translator import translator, TranslationOptions

from portal.models import Approach, ApproachSector, PracticeArea, Language, Award, PageParameter, Page, Office, \
	SiteParameter, Opportunity, PublicationType, Publication, Event, SpecializationSector, SocialEntity, Contact, Values


@register(SiteParameter)
class SiteParameterTranslation(TranslationOptions):
	fields = ["value", "file"]


@register(Page)
class PageTranslation(TranslationOptions):
	fields = ["title"]


@register(PageParameter)
class PageParameterTranslation(TranslationOptions):
	fields = ["value"]


@register(PracticeArea)
class PracticeAreaTranslation(TranslationOptions):
	fields = ["name", "description"]


@register(SpecializationSector)
class PracticeAreaTranslation(TranslationOptions):
	fields = ["name", "description"]


@register(Approach)
class ApproachTranslation(TranslationOptions):
	fields = ["text"]

@register(ApproachSector)
class ApproachSectorTranslation(TranslationOptions):
	fields = ["text"]

@register(Language)
class LanguageTranslation(TranslationOptions):
	fields = ["name"]


@register(Award)
class AwardTranslation(TranslationOptions):
	fields = ["title", "description"]


@register(Office)
class OfficeTranslation(TranslationOptions):
	fields = ["country", "state", "city", "address", "neighborhood"]


@register(Opportunity)
class OpportunityTranslation(TranslationOptions):
	fields = ["title", "city", "description_short", "description"]


@register(PublicationType)
class PublicationTypeTranslation(TranslationOptions):
	fields = ["name"]


@register(Publication)
class PublicationTranslation(TranslationOptions):
	fields = ["title", "description_short", "description", "file"]


@register(Event)
class EventTranslation(TranslationOptions):
	fields = ["description_short", "country", "city", "address"]


@register(SocialEntity)
class SocialEntityTranslation(TranslationOptions):
	fields = ["description"]

@register(Contact)
class ContactTranslation(TranslationOptions):
	fieds= ["name", "telefone", "email", "message"]

@register(Values)
class ContactTranslation(TranslationOptions):
	fieds= ["title", "description"]