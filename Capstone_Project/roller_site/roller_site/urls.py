"""roller_site URL Configuration

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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "roller_app.views.index"),
    url(r'^api_dice/$', "roller_app.views.api_dice"),
    url(r'^api_dice_roll/(?P<number>[0-9]+)/$', "roller_app.views.api_dice_roll"),
    url(r'^login/$', 'roller_app.views.login_view'),
    url(r'^register/$', 'roller_app.views.register_view'),
    url(r'^api_newCharacter/$', "roller_app.views.api_newCharacter"),
    url(r'^logout_view/$', "roller_app.views.logout_view"),


]
