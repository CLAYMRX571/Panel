from modeltranslation.translator import register, TranslationOptions
from .models import Employ

@register(Employ)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'title', 'value', 'value_name', 'value_desc', 'strategy_name', 'strategy_title',)