"""test_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from test_task_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.shortener_view, name='shortener-form'),
    url(r'^i/(?P<slug>.+)$', views.InfoView.as_view(), name='info'),
    url(r'^r/(?P<slug>.+)$', views.redirect_view, name='redirect'),
    url(r'^popular/', views.PopularView.as_view(), name='popular'),
    url(r'^d/(?P<slug>.+)$', views.UrlDelete.as_view(), name='delete')
]