from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Plan

@admin.register(Plan)
class PlanAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'long_desc',]
