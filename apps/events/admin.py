from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Events, Elent

@admin.register(Events)
class EventsAdmin(TranslationAdmin):
    list_display = ['name', 'location', 'title',]

@admin.register(Elent)
class ElentAdmin(TranslationAdmin):
    list_display = ['name', 'desc',]