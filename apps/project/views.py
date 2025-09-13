from django.shortcuts import render, redirect
from .models import Project

def ProjectViews(request):
    project = Project.objects.all()  

    context = {
        'project': project,
    }

    return render(request, 'project.html', context)

def lan_switch_project(request, lan):
    return redirect(f'/{lan}/project/')