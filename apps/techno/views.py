from django.shortcuts import render, redirect
from .models import Techno

def TechnoViews(request):
    techno = Techno.objects.all()  

    context = {
        'techno': techno,
    }

    return render(request, 'techno.html', context)

def lan_switch_techno(request, lan):
    return redirect(f'/{lan}/techno/')