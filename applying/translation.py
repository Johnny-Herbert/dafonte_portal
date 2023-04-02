from modeltranslation.decorators import register
from modeltranslation.translator import translator, TranslationOptions

from applying.models import *

translator.register(Application)
translator.register(ProfessionalExperience)
translator.register(Academic)
translator.register(ApplicationLanguage)