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
from apps.events.views import Eventviews, lan_switch_event
from apps.data.views import Dataviews, lan_switch_data
from apps.education.views import Educationviews, lan_switch_education
from apps.part.views import PartViews, lan_switch_part
from apps.project.views import ProjectViews, lan_switch_project
from apps.innovation.views import Innoviews, lan_switch_inno
from apps.outlook.views import OutlookViews, lan_switch_outlook
from apps.planning.views import PlanViews, lan_switch_plan
from apps.policy.views import PolicyViews, lan_switch_policy
from apps.techno.views import TechnoViews, lan_switch_techno

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('lan/<str:lan>/', lan_switch, name='lan_switch'),
    path('lan/about/<str:lan>/', lan_switch_about, name='lan_switch_about'),
    path('lan/membership/<str:lan>/', lan_switch_membership, name='lan_switch_membership'),
    path('lan/news/<str:lan>/', lan_switch_news, name='lan_switch_news'),
    path('lan/event/<str:lan>/', lan_switch_event, name='lan_switch_event'),
    path('lan/data/<str:lan>/', lan_switch_data, name='lan_switch_data'),
    path('lan/education/<str:lan>/', lan_switch_education, name='lan_switch_education'),
    path('lan/part/<str:lan>/', lan_switch_part, name='lan_switch_part'),
    path('lan/project/<str:lan>/', lan_switch_project, name='lan_switch_project'),
    path('lan/inno/<str:lan>/', lan_switch_inno, name='lan_switch_inno'),
    path('lan/outlook/<str:lan>/', lan_switch_outlook, name='lan_switch_outlook'),
    path('lan/plan/<str:lan>/', lan_switch_plan, name='lan_switch_plan'),
    path('lan/policy/<str:lan>/', lan_switch_policy, name='lan_switch_policy'),
    path('lan/techno/<str:lan>/', lan_switch_techno, name='lan_switch_techno'),
    # path('lan/education/<str:lan>/', lan_switch_education, name='lan_switch_education'),
    # path('lan/education/<str:lan>/', lan_switch_education, name='lan_switch_education'),
    # path('lan/education/<str:lan>/', lan_switch_education, name='lan_switch_education'),
    # path('lan/education/<str:lan>/', lan_switch_education, name='lan_switch_education'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', Homeviews, name='index'),
    path('about/', AboutViews, name='about'),
    path('membership/', Membershipviews, name='membership'),
    path('news/', Newsviews, name='news'),
    path('event/', Eventviews, name='event'),
    path('data/', Dataviews, name='data'),
    path('education/', Educationviews, name='education'),
    path('part/', PartViews, name='part'),
    path('project/', ProjectViews, name='project'),
    path('inno/', Innoviews, name='inno'),
    path('outlook/', OutlookViews, name='outlook'),
    path('plan/', PlanViews, name='plan'),
    path('policy/', PolicyViews, name='policy'),
    path('techno/', TechnoViews, name='techno'),
    # path('education/', Educationviews, name='education'),
    # path('education/', Educationviews, name='education'),
    # path('education/', Educationviews, name='education'),
    # path('education/', Educationviews, name='education'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)