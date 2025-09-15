from modeltranslation.translator import register, TranslationOptions
from .models import Education

@register(Education)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'see_more', 'category_name', 'desc', 'edu_name', 'edu_desc',)