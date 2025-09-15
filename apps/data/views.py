from django.shortcuts import render, redirect
from .models import Data, Related

def Dataviews(request):
    data = Data.objects.all()  
    related = Related.objects.all()

    context = {
        'data': data,
        'related': related,
    }

    return render(request, 'data.html', context)

def lan_switch_data(request, lan):
    return redirect(f'/{lan}/data/')