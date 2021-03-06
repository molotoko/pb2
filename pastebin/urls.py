"""pastebin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from views import paste_list, paste_detail, create_paste, main, search


urlpatterns = [
    url(r'^admin/',                 include(admin.site.urls)),
    url(r'^$',                      main, name='main'),
    url(r'^paste/$',                paste_list, name='paste_list'),
    url(r'^add/$',                  create_paste, name='create_paste'),
    url(r'^search/$',               search),
    #url(r'^register/$', 'registration.views.register', {'form': RegistrationFormUniqueEmail}, name='registration_register'),
    #url(r'^accounts/$'),            include('registration.urls'),
    url(r'^accounts/',              include('registration.backends.simple.urls')),
    url(r'^([0-9a-z-]+)/$',         paste_detail, name='paste_detail'),

]
