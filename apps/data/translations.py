from modeltranslation.translator import register, TranslationOptions
from .models import Data, Related

@register(Data)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'more_name', 'desc', 'title', 'title_desc', 'file_name',)

@register(Related)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('relate_name', 'relate_more', 'relate_title',)