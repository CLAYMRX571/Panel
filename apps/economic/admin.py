from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Eco

@admin.register(Eco)
class EcoAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'eco_desc',]