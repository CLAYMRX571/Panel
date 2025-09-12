from django.shortcuts import render, redirect
from .models import Education

def Educationviews(request):
    education = Education.objects.all()  

    context = {
        'education': education,
    }

    return render(request, 'education.html', context)

def lan_switch_education(request, lan):
    return redirect(f'/{lan}/education/')