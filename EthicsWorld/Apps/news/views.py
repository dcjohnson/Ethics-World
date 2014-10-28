from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Apps.news.models import News
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
        return HttpResponse(request.POST['newsurl'])
    finally:
        return HttpResponseRedirect(reverse("news:index"))
