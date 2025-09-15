from django.shortcuts import render, redirect
from .models import Eco

def Ecoviews(request):
    eco = Eco.objects.all()  

    context = {
        'eco': eco,
    }

    return render(request, 'eco.html', context)

def lan_switch_eco(request, lan):
    return redirect(f'/{lan}/eco/')