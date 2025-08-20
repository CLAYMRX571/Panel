from modeltranslation.translator import register, TranslationOptions
from .models import Indexs

@register(Indexs)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'about_name', 'about_desc', 'service_name', 'service_desc', 'project_name', 'project_desc', 'team_name', 'team_jobs')