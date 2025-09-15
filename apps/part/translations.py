from modeltranslation.translator import register, TranslationOptions
from .models import Part

@register(Part)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)