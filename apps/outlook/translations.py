from modeltranslation.translator import register, TranslationOptions
from .models import About

@register(About)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'adverb_name', 'adverb_desc', 'adverb_more',)