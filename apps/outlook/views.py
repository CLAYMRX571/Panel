from django.shortcuts import render, redirect
from .models import Outlook

def OutlookViews(request):
    outlook = Outlook.objects.all()  

    context = {
        'outlook': outlook,
    }

    return render(request, 'outlook.html', context)

def lan_switch_outlook(request, lan):
    return redirect(f'/{lan}/outlook/')
