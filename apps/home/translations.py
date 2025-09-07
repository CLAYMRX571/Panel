from modeltranslation.translator import register, TranslationOptions
from .models import Home, News, Publication, Event, Video

@register(Home)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'button_name', 'abouts_button', 'more_button', 'support_desc', 'search_name')
    
@register(News)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'desc', 'tag')
    
@register(Publication)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'meta', 'view')
    
@register(Event)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'location') 

@register(Video)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'desc', 'author', 'role', 'more') 
