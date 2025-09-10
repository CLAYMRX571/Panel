from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import About

@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'adverb_name', 'adverb_desc', 'adverb_more',]
