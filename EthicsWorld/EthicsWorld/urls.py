from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'Apps.home.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^forum/', include('Apps.forum.urls' , namespace = 'forum')),
    url(r'^news/', include('Apps.news.urls', namespace = 'news'))
)
