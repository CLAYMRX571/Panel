from modeltranslation.translator import register, TranslationOptions
from .models import News, NewsAdver

@register(News)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', 'all_name', 'title', 'desc',)

@register(NewsAdver)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'button_name', 'desc',) 