from django.shortcuts import render, redirect
from .models import News, NewsAdver

def Newsviews(request):
    news = News.objects.all()  
    newsadver = NewsAdver.objects.all()

    context = {
        'news': news,
        'newsadver': newsadver,
    }

    return render(request, 'news.html', context)

def lan_switch_news(request, lan):
    return redirect(f'/{lan}/news/')
