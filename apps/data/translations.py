from modeltranslation.translator import register, TranslationOptions
from .models import Data

@register(Data)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'title', 'title_desc', 'file', 'relate', 'relate_link', 'relate_desc',)