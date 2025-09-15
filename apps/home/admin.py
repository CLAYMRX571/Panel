from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Banner, Home, Mission, Latest, Adver

@admin.register(Banner)
class BannerAdmin(TranslationAdmin):
    list_display = ['name',]

@admin.register(Home)
class HomeAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'button_name', 'buttons_name', 'buttons_desc',]

@admin.register(Mission)
class MissionAdmin(TranslationAdmin):
    list_display = ['mission_title', 'mission_desc', 'mission_button_name', 'mission_label', 'mission_detail',]
    
@admin.register(Latest)
class LatestAdmin(TranslationAdmin):
    list_display = ['category_name', 'browse_link_name', 'latest_image', 'latest_title', 'latest_desc',]
    
@admin.register(Adver)
class AdverAdmin(TranslationAdmin):
    list_display = ['name', 'title', 'button_name', 'desc',]