from django.db import models

class News(models.Model):
	newsLink = models.URLField()
	newsText = models.TextField()
	newsDate = models.DateTimeField(auto_now_add = True)
	newsHash = models.CharField(max_length = 40)

class Discussion(models.Model):
	discussionText = models.TextField()
	discussionDate = models.DateTimeField(auto_now_add = True)
	discussionHash = models.CharField(max_length = 40)
