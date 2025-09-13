from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProjectViews, name='project'),
]