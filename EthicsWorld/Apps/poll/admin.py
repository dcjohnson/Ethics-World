from django.contrib import admin
from Apps.poll.models import Question
from Apps.poll.models import AvaliableAnswers
from Apps.poll.models import Answer

admin.site.register(Question)
admin.site.register(AvaliableAnswers)
admin.site.register(Answer)
