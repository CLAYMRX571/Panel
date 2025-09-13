from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Employ

@admin.register(Employ)
class EmployAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'title', 'value', 'value_name', 'value_desc', 'strategy_name', 'strategy_title',]