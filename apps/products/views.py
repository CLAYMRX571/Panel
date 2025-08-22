from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Indexs

class HomesView(View):
    def get(self, request):
        return render(request, "index.html") 

def lan_switch(request, lan):
    return redirect(f'/{lan}/')