from modeltranslation.translator import register, TranslationOptions
from .models import Project

@register(Project)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc',)