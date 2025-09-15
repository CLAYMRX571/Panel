from modeltranslation.translator import register, TranslationOptions
from .models import Plan

@register(Plan)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'long_desc',)