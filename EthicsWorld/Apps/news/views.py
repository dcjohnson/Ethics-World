from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Apps.news.models import News, Discussion
from common import helpers

def Index(request):
    sqlData = News.objects.all()
    htmlData = {
        'newsreports':sqlData
    }
    return render(request, 'newsindex.html', htmlData)

def AddNews(request):
    try:
        newNews = News()
        newNews.newsLink = request.POST['newsurl']
        newNews.newsText = request.POST['newsinformation']
        newNews.newsHash = helpers.GetHash(request.POST['newsurl'])
        newNews.save()
    finally:
        return HttpResponseRedirect(reverse("news:index"))

def AddComment(request):
    try:
        newComment = Discussion()
        newComment.discussionText = request.POST['commenttext']
        newComment.discussionHash = helpers.GetHash(request.POST['commenttext'])
        newComment.discussionNewsHash = request.POST['newshash']
        newComment.save()
    finally:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def CommentPage(request):
    try:
        newsData = News.objects.get(newsHash = request.GET['newsHash'])
        commentData = Discussion.objects.filter(discussionNewsHash = request.GET['newsHash'])
        htmlData = {
            'newsdata':newsData,
            'commentdata':commentData
        }
        return render(request, 'commentsection.html', htmlData)
    except:
        return HttpResponseRedirect(reverse("news:index"))
