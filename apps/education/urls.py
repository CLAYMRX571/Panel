from django.urls import path
from . import views

urlpatterns = [
    path('', views.Educationviews, name='education'),
]