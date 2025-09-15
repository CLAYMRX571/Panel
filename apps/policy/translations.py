from modeltranslation.translator import register, TranslationOptions
from .models import Policy

@register(Policy)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'policy_desc',)