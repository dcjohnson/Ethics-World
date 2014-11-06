from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Apps.forum.models import Issue, Responses
from common import helpers

def Index(request):
    sqlData = Issue.objects.all()
    htmlData = {
        'questions' : sqlData,
    }
    return render(request, 'forum/forumindex.html', htmlData)

def IndividualQuestionPage(request):
    try:
        sqlIssueData = Issue.objects.get(issueHash = request.GET['questionHash'])
        sqlResponsesData = Responses.objects.filter(responsesIssueHash = request.GET['questionHash'])
        htmlData = {
            'question':sqlIssueData,
            'answers':sqlResponsesData,
        }
        return render(request, 'forum/individualquestion.html', htmlData)
    except:
        return HttpResponseRedirect(reverse("forum:index"))

def CreateComment(request):
    try:
        newComment = Responses()
        newComment.responsesIssueHash = request.POST['issueHash']
        newComment.responsesResponse = request.POST['comment']
        newComment.responsesHash = helpers.GetHash(request.POST['comment'])
        newComment.save()
    finally:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def CreateQuestion(request):
    try:
        newIssue = Issue()
        newIssue.issueQuestion = request.POST['question']
        newIssue.issueHash = helpers.GetHash(request.POST['question'])
        newIssue.save()
    finally:
        return HttpResponseRedirect(reverse("forum:index"))
