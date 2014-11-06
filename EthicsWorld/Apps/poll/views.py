from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from Apps.poll.models import Question, AvaliableAnswers, Answer
from common import helpers

def Index(request):
    pollData = Question.objects.all()
    htmlData = {
        'polls':pollData
    }
    return render(request, "pollindex.html", htmlData)

def IndividualPoll(request):
    try:
        pollData = Question.objects.get(questionHash = request.GET['pollhash'])
        answerData = AvaliableAnswers.objects.filter(avaliableAnswersQuestionHash = request.GET['pollhash'])
        htmlData = {
            'poll':pollData,
            'avaliableanswers':answerData
        }
        return render(request, "individualpoll.html", htmlData)
    except:
        return HttpResponseRedirect(reverse("poll:index"))

def MakePoll(request):
    try:
        questionHash = helpers.GetHash(request.POST['polltext'])
        newQuestion = Question()
        newQuestion.questionText = request.POST['polltext']
        newQuestion.questionHash = questionHash
        newQuestion.save()
        newAnswers = request.POST.getlist('pollanswer')
        for answer in newAnswers:
            newAnswerModel = AvaliableAnswers()
            newAnswerModel.avaliableAnswersHash = helpers.GetHash(answer)
            newAnswerModel.avaliableAnswersText = answer
            newAnswerModel.avaliableAnswersQuestionHash = questionHash
            newAnswerModel.save()
    finally:
        return HttpResponseRedirect(reverse("poll:index"))
