from django.conf.urls import patterns, url

from Apps.news import views

urlpatterns = patterns('',
    url(r'^$', views.Index, name = 'index'),
    url(r'^addnews/$', views.AddNews, name = 'addnews'),
    url(r'^commentpage/$', views.CommentPage, name = 'commentpage'),
    url(r'^addcomment/$', views.AddComment, name = 'createcomment')
)
