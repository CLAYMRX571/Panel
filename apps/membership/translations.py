from modeltranslation.translator import register, TranslationOptions
from .models import Membership

@register(Membership)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'members_title', 'country_name', 'disclaimer_name', 'disclaimer_desc',)