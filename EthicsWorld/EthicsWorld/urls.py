from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'EthicsWorld.views.index', name = 'index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^forum/', include('Apps.forum.urls')),
)
