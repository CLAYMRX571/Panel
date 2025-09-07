from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Home, News, Publication, Event, Video

@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button_name', 'abouts_button', 'more_button', 'support_desc', 'search_name',]

@admin.register(News)
class NewAdmin(TranslationAdmin):
    list_display = ['title', 'desc', 'tag', ]

@admin.register(Publication)
class PublicationAdmin(TranslationAdmin):
    list_display = ['name', 'title', 'meta', 'view', ]
    
@admin.register(Event)
class EventAdmin(TranslationAdmin):
    list_display = ['title', 'location', ]
    
@admin.register(Video)
class VideoAdmin(TranslationAdmin):
    list_display = ['title', 'desc', 'author', 'role', 'more', ]