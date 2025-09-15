from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Finance

@admin.register(Finance)
class FinanceAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'finance_desc',]