from django.shortcuts import render, redirect
from .models import Policy

def PolicyViews(request):
    policy = Policy.objects.all()  

    context = {
        'policy': policy,
    }

    return render(request, 'policy.html', context)

def lan_switch_policy(request, lan):
    return redirect(f'/{lan}/policy/')
