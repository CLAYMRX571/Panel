from django.urls import path
from . import views

urlpatterns = [
    path('', views.Ecoviews, name='eco'),
]