from django.conf.urls import patterns, url

from Apps.forum import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^createquestion/$', views.createquestion, name = 'createquestion'),
)
