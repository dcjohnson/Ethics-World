# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('responsesIssueHash', models.CharField(max_length=40)),
                ('responsesResponse', models.TextField()),
                ('responsesDate', models.DateTimeField(verbose_name='Response Date')),
                ('responsesHash', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='issue',
            name='issueDate',
            field=models.DateTimeField(verbose_name='Issue Date'),
        ),
    ]
