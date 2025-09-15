from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Data, Related

@admin.register(Data)
class DataAdmin(TranslationAdmin):
    list_display = ['name', 'more_name', 'desc', 'title', 'title_desc', 'file_name',]

@admin.register(Related)
class RelatedAdmin(TranslationAdmin):
    list_display = ['relate_name', 'relate_more', 'relate_title',]