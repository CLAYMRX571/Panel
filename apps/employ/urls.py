from django.urls import path
from . import views

urlpatterns = [
    path('', views.Employviews, name='employ'),
]