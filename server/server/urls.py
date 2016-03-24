"""server URL Configuration

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
from django.conf.urls import include, patterns, url
from django.shortcuts import redirect
from django.http import Http404

from redis_init import redis


def check_redirect(request, tiny_id):
    link = redis.get('tiny_id_{}'.format(tiny_id))
    if link:
        return redirect(link)
    else:
        raise Http404("Link doesn't exist")


urlpatterns = [
    url(r'^api/', include('tiny.urls')),
    url(r'^(?P<tiny_id>.*)/$', check_redirect),
]

urlpatterns += patterns(
    'django.contrib.staticfiles.views',
    url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'index.html'})
)
