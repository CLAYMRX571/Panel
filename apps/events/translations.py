from modeltranslation.translator import register, TranslationOptions
from .models import Events, Elent

@register(Events)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'location', 'title',)

@register(Elent)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)