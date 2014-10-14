# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('answerQuestionHash', models.CharField(max_length=40)),
                ('answerChoiceHash', models.CharField(max_length=40)),
                ('answerDateResponded', models.DateTimeField(verbose_name='Date Answered')),
                ('answerIPOfAnswerer', models.GenericIPAddressField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AvaliableAnswers',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('avaliableAnswersQuestionHash', models.CharField(max_length=40)),
                ('avaliableAnswersText', models.CharField(max_length=200)),
                ('avaliableAnswersHash', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('questionText', models.TextField()),
                ('quesiionDate', models.DateTimeField(verbose_name='Question Date')),
                ('questionHash', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
