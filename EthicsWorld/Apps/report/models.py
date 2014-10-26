from django.db import models

class Report(models.Model):
    reportIncedentHash = models.CharField(max_length = 40)
    reportDate = models.DateTimeField(auto_now_add = True)
    reportReason = models.TextField()
    reportIsHandeled = models.BooleanField(default = False)
    reportHash = models.CharField(max_length = 40)
