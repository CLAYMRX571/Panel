from django.shortcuts import render, redirect
from .models import Home, News, Publication, Event, Video

def Homeviews(request):
    home = Home.objects.all()  
    news_list = News.objects.all()
    publications = Publication.objects.all()
    events = Event.objects.all()
    videos = Video.objects.all()

    context = {
        'home': home,
        'news_list': news_list,
        'publications': publications,
        'events': events,
        'videos': videos,
    }

    return render(request, 'index.html', context)

def lan_switch(request, lan):
    return redirect(f'/{lan}/')