from django.db import models

class Issue(models.Model):
	issueQuestion = models.TextField()
	issueDate = models.DateTimeField('Issue Date')
	issueHash = models.CharField(max_length = 40)

class Responses(models.Model):
	responsesIssueHash = models.CharField(max_length = 40)
	responsesResponse = models.TextField()
	responsesDate = models.DateTimeField('Response Date')
	responsesHash = models.CharField(max_length = 40)
