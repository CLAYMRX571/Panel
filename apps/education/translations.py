from modeltranslation.translator import register, TranslationOptions
from .models import Education

@register(Education)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'category_name', 'desc', 'technical_name', 'technical_desc',)