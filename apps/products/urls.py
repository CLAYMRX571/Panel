from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomesView, name="index"),
    path("lan/<str:lan>/", views.lan_switch, name="lan_switch"),
]