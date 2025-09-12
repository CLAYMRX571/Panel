from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Data

@admin.register(Data)
class DataAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title', 'title_desc', 'file', 'relate', 'relate_link', 'relate_desc',]