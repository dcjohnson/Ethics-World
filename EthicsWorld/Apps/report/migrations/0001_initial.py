# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('reportIncedentHash', models.CharField(max_length=40)),
                ('reportDate', models.DateTimeField(max_length=40)),
                ('reportReason', models.TextField()),
                ('reportIsHandeled', models.BooleanField(default=False)),
                ('reportHash', models.CharField(max_length=40)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
