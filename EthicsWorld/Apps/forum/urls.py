from django.conf.urls import patterns, url

from Apps.forum import views

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
    url(r'^createquestion/$', views.CreateQuestion, name = 'createquestion'),
    url(r'^individualquestion/$', views.IndividualQuestionPage, name = 'individualquestion'),
    url(r'^createcomment/$', views.CreateComment, name = 'createcomment')
)
