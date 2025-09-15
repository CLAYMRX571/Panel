from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Policy

@admin.register(Policy)
class PolicyAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'policy_desc',]
