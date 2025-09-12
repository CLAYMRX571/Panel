from django.shortcuts import render, redirect
from .models import Data

def Dataviews(request):
    data = Data.objects.all()  

    context = {
        'data': data,
    }

    return render(request, 'data.html', context)

def lan_switch_data(request, lan):
    return redirect(f'/{lan}/data/')