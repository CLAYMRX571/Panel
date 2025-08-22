from django.urls import path
from .views import HomesView, lan_switch

urlpatterns = [
    path("", HomesView.as_view(), name="index"),
    path("lan/<str:lan>/", lan_switch, name="lan_switch"),
]