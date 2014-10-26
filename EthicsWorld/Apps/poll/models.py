from django.db import models

class Question(models.Model):
    questionText = models.TextField()
    quesiionDate = models.DateTimeField(auto_now_add = True)
    questionHash = models.CharField(max_length = 40)

class AvaliableAnswers(models.Model):
    avaliableAnswersQuestionHash = models.CharField(max_length = 40)
    avaliableAnswersText = models.CharField(max_length = 200)
    avaliableAnswersHash = models.CharField(max_length = 40)

class Answer(models.Model):
    answerQuestionHash = models.CharField(max_length = 40)
    answerChoiceHash = models.CharField(max_length = 40)
    answerDateResponded = models.DateTimeField(auto_now_add = True)
    answerIPOfAnswerer = models.GenericIPAddressField()
