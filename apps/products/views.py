from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Indexs

class HomesView(View):
    def get(self, request):
        return render(request, "index.html") 

class Lang(View):
    def get(self, request, lan):
        return redirect(f'/{lan}/')