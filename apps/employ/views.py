from django.shortcuts import render, redirect
from .models import Employ

def Employviews(request):
    employ = Employ.objects.all()  

    context = {
        'employ': employ,
    }

    return render(request, 'employ.html', context)

def lan_switch_employ(request, lan):
    return redirect(f'/{lan}/employ/')