from django.urls import path
from . import views

urlpatterns = [
    path('', views.PartViews, name='part'),
]