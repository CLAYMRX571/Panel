from django.shortcuts import render, redirect
from .models import Finance

def Financeviews(request):
    finance = Finance.objects.all()  

    context = {
        'finance': finance,
    }

    return render(request, 'finance.html', context)

def lan_switch_finance(request, lan):
    return redirect(f'/{lan}/finance/')