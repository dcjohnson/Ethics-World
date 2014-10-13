from django.db import models

class News(models.Model):
	newsLink = models.URLField()
	newsText = models.TextField()
	newsDate = models.DateTimeField('Date Posted')
	newsHash = models.CharField(max_length = 40)

class Discussion(models.Model):
	discussionText = models.TextField()
	discussionDate = models.DateTimeField('Date Posted')
	discussionHash = models.CharField(max_length = 40)