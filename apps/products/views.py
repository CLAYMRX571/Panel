from django.shortcuts import render, redirect
from django.views.generic import View

class HomesView(View):
    def get(self, request):
        context = {
            "indexes": []
        }
        return render(request, "index.html", context)

def lan_switch(request, lan):
    return redirect(f'/{lan}/')