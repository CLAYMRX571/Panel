from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Outlook

@admin.register(Outlook)
class OutlookAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'focus_name', 'focus_desc',]
