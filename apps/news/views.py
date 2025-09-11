from django.shortcuts import render, redirect
from .models import News

def Newsviews(request):
    news = News.objects.all()  

    context = {
        'news': news,
    }

    return render(request, 'news.html', context)

def lan_switch_news(request, lan):
    return redirect(f'/{lan}/news/')
