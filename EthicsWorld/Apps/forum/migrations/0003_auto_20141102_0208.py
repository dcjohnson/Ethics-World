# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20141014_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='issueDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='responses',
            name='responsesDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
