from modeltranslation.translator import register, TranslationOptions
from .models import Inno

@register(Inno)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)