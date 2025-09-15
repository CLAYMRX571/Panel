from modeltranslation.translator import register, TranslationOptions
from .models import Eco

@register(Eco)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'eco_desc',)