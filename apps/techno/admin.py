from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Techno

@admin.register(Techno)
class PolicyAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'techno_desc',]
