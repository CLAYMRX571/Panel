from django.urls import path
from .views import HomesView, Lang

urlpatterns = [
    path("", HomesView.as_view(), name="index"),
    path("lan/<str:lan>/", Lang.as_view(), name="lan_switch"),
]