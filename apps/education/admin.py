from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Education

@admin.register(Education)
class EducationAdmin(TranslationAdmin):
    list_display = ['name', 'category_name', 'desc', 'technical_name', 'technical_desc',]