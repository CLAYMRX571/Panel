from django.shortcuts import render, redirect
from .models import Banner, Home, Mission, Latest, Adver

def Homeviews(request):
    banner = Banner.objects.all()
    home = Home.objects.all()
    mission = Mission.objects.all()
    latest = Latest.objects.all()
    adver = Adver.objects.all()

    context = {
        'banner': banner,
        'home': home,
        'mission': mission,
        'latest': latest,
        'adver': adver,
    }

    return render(request, 'index.html', context)

def lan_switch(request, lan):
    return redirect(f'/{lan}/')