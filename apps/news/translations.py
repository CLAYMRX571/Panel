from modeltranslation.translator import register, TranslationOptions
from .models import News

@register(News)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'links_name', 'title', 'title_link',)