from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Indexs

class HomesView(ListView):
    model = Indexs
    context_object_name = 'indexes'
    template_name = 'index.html'

def lan_switch(request, lan):
    return redirect(f'/{lan}/')