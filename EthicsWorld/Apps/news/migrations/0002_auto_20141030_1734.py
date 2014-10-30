# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='discussionNewsHash',
            field=models.CharField(default=datetime.date(2014, 10, 30), max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discussion',
            name='discussionDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='newsDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
