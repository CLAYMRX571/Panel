from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import News

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'links_name', 'title', 'title_link',]
