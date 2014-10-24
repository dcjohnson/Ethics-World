from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Apps.forum.models import Issue
import hashlib

def GetHash(rawString):
    newHash = hashlib.sha1()
    newHash.update(bytes(rawString, encoding = 'utf-8'))
    return newHash.hexdigest()

def index(request):
    return render(request, 'index.html')

def createquestion(request):
    try:
        newIssue = Issue()
        newIssue.issueQuestion = request.POST['question']
        newIssue.issueHash = GetHash(request.POST['question'])
        newIssue.save()
        return HttpResponseRedirect(reverse("forum:index"))
    except:
        return HttpResponse("FAIL")
