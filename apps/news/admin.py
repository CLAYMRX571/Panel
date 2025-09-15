from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import News, NewsAdver

@admin.register(News)
class NewsAdmin(TranslationAdmin):
    list_display = ['category_name', 'all_name', 'title', 'desc',]

@admin.register(NewsAdver)
class NewsAdmin(TranslationAdmin):
    list_display = ['name', 'title', 'button_name', 'desc',]