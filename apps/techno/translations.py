from modeltranslation.translator import register, TranslationOptions
from .models import Techno

@register(Techno)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'techno_desc',)