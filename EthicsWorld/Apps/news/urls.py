from django.conf.urls import patterns, url

from Apps.news import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index')
)
