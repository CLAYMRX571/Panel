from django.shortcuts import render, redirect
from .models import Events, Elent

def Eventviews(request):
    event = Events.objects.all()  
    elent = Elent.objects.all()

    context = {
        'event': event,
        'elent': elent,
    }

    return render(request, 'events.html', context)

def lan_switch_event(request, lan):
    return redirect(f'/{lan}/event/')