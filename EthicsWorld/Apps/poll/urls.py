from django.conf.urls import patterns, url

from Apps.poll import views

urlpatterns = patterns('',
    url(r'^$', views.Index, name = 'index'),
    url(r'^indivpoll/$', views.IndividualPoll, name = 'indivpoll'),
    url(r'^newpoll/$', views.MakePoll, name = 'makepoll'),
    url(r'^newpollresponse/$', views.GetPollResponse, name = 'newpollresponse'),
    url(r'^pollstats/$', views.RenderPollStats, name = 'pollstats')
)
