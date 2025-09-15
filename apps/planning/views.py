from django.shortcuts import render, redirect
from .models import Plan

def PlanViews(request):
    plan = Plan.objects.all()  

    context = {
        'plan': plan,
    }

    return render(request, 'plan.html', context)

def lan_switch_plan(request, lan):
    return redirect(f'/{lan}/plan/')
