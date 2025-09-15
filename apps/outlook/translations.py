from modeltranslation.translator import register, TranslationOptions
from .models import Outlook

@register(Outlook)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'focus_name', 'focus_desc',)