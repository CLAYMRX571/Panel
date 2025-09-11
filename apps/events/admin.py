from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Events

@admin.register(Events)
class EventsAdmin(TranslationAdmin):
    list_display = ['name', 'title', 'events_name', 'events_desc',]