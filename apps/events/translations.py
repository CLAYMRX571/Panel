from modeltranslation.translator import register, TranslationOptions
from .models import Events

@register(Events)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'events_name', 'events_desc',)