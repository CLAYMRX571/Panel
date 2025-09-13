from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Inno

@admin.register(Inno)
class InnoAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]
