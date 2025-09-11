from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import eve, News, Publication, Event, Video

@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    list_display = ['name', 'title', 'events_name', 'events_desc',]