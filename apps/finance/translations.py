from modeltranslation.translator import register, TranslationOptions
from .models import Finance

@register(Finance)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'finance_desc',)