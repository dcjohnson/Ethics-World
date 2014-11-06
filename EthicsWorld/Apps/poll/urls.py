from django.conf.urls import patterns, url

from Apps.poll import views

urlpatterns = patterns('',
    url(r'^$', views.Index, name = 'index'),
    url(r'^indivpoll/$', views.IndividualPoll, name = 'indivpoll'),
    url(r'^newpoll/$', views.MakePoll, name = 'makepoll')
)
