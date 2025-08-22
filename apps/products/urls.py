from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomesView, name="index"),
    path("lan/<str:lan>/", views.Lang, name="lan_switch"),
]