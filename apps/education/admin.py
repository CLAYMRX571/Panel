from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Education

@admin.register(Education)
class EducationAdmin(TranslationAdmin):
    list_display = ['name', 'see_more', 'category_name', 'desc', 'edu_name', 'edu_desc',]