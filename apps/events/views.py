from django.shortcuts import render, redirect
from .models import Events

def Eventviews(request):
    event = Events.objects.all()  

    context = {
        'event': event,
    }

    return render(request, 'events.html', context)

def lan_switch_event(request, lan):
    return redirect(f'/{lan}/event/')