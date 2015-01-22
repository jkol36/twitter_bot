# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_bot', '0002_twitterstatus_hashtags'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='twitter_user',
            field=models.ManyToManyField(related_name='hashtags', null=True, to='twitter_bot.TwitterUser', blank=True),
            preserve_default=True,
        ),
    ]
