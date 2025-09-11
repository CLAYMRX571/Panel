"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from apps.home.views import Homeviews, lan_switch
from apps.about.views import AboutViews, lan_switch_about
from apps.membership.views import Membershipviews, lan_switch_membership
from apps.news.views import Newsviews, lan_switch_news

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('lan/<str:lan>/', lan_switch, name='lan_switch'),
    path('lan/about/<str:lan>/', lan_switch_about, name='lan_switch_about'),
    path('lan/membership/<str:lan>/', lan_switch_membership, name='lan_switch_membership'),
    path('lan/news/<str:lan>/', lan_switch_news, name='lan_switch_news'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', Homeviews, name='index'),
    path('about/', AboutViews, name='about'),
    path('membership/', Membershipviews, name='membership'),
    path('news/', Newsviews, name='news'),
    # path('data/', include('apps.data.urls')),
    # path('education/', include('apps.education.urls')),
    # path('energy/', include('apps.energy.urls')),
    # path('events/', include('apps.events.urls')),
    # path('publications/', include('apps.publications.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)