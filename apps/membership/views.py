from django.shortcuts import render, redirect
from .models import Membership

def Membershipviews(request):
    membership = Membership.objects.all()  

    context = {
        'membership': membership,
    }

    return render(request, 'membership.html', context)

def lan_switch_membership(request, lan):
    return redirect(f'/{lan}/membership/')
