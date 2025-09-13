from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Part

@admin.register(Part)
class PartAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title',]
