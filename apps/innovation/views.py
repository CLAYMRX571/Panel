from django.shortcuts import render, redirect
from .models import Inno

def Innoviews(request):
    inno = Inno.objects.all()  

    context = {
        'inno': inno,
    }

    return render(request, 'innovation.html', context)

def lan_switch_inno(request, lan):
    return redirect(f'/{lan}/inno/')