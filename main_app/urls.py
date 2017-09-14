"""IPL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main_app import views
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^index', views.index),
    url(r'^result', views.result),
    url(r'^schedule', views.schedule),
    url(r'^detail/(?P<tid>[0-9]+)/', views.detail,name='detail'),
    url(r'^teams', views.teams),
    url(r'^stats', views.stats),
    url(r'^contactus', views.contactus),
#    url(r'^forum', views.forum),
    url(r'^post_enquiries/$',views.post_enquiry,name='post_enquiry'),
#    url(r'^post_messages/$',views.post_messages,name='post_messages')
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    ]
