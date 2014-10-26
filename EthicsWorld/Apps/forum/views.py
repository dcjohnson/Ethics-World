from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Apps.forum.models import Issue, Responses
import hashlib


def GetHash(rawString):
    newHash = hashlib.sha1()
    newHash.update(bytes(rawString, encoding = 'utf-8'))
    return newHash.hexdigest()

def index(request):
    sqlData = Issue.objects.all()
    htmlData = {
        'questions' : sqlData,
    }
    return render(request, 'index.html', htmlData)

def IndividualQuestionPage(request):
    try:
        sqlIssueData = Issue.objects.get(issueHash = request.GET['questionHash'])
        sqlResponsesData = Responses.objects.filter(responsesIssueHash = request.GET['questionHash'])
        htmlData = {
            'question':sqlIssueData,
            'answers':sqlResponsesData,
        }
        return render(request, 'individualquestion.html', htmlData)
    except:
        return HttpResponseRedirect(reverse("forum:index"))

def CreateComment(request):
    try:
        newComment = Responses()
        newComment.responsesIssueHash = request.POST['issueHash']
        newComment.responsesResponse = request.POST['comment']
        newComment.responsesHash = GetHash(request.POST['comment'])
        newComment.save()
    finally:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def CreateQuestion(request):
    try:
        newIssue = Issue()
        newIssue.issueQuestion = request.POST['question']
        newIssue.issueHash = GetHash(request.POST['question'])
        newIssue.save()
    finally:
        return HttpResponseRedirect(reverse("forum:index"))
