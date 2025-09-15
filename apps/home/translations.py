from modeltranslation.translator import register, TranslationOptions
from .models import Banner, Home, Mission, Latest, Adver

@register(Banner)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
    
@register(Home)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button_name', 'buttons_name', 'buttons_desc',)
    
@register(Mission)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('mission_title', 'mission_desc', 'mission_button_name', 'mission_label', 'mission_detail',)
    
@register(Latest)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name', 'browse_link_name', 'latest_image', 'latest_title', 'latest_desc',) 

@register(Adver)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'button_name', 'desc',) 
