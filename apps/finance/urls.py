from django.urls import path
from . import views

urlpatterns = [
    path('', views.Financeviews, name='finance'),
]