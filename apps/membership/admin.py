from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Membership

@admin.register(Membership)
class MembershipAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'members_title', 'country_name', 'disclaimer_name', 'disclaimer_desc',]
