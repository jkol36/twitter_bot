# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterstatus',
            name='hashtags',
            field=models.ManyToManyField(related_name='statuses', null=True, to='twitter_bot.hashtag', blank=True),
            preserve_default=True,
        ),
    ]
