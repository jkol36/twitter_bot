# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_bot', '0004_remove_hashtag_twitter_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitterstatus',
            name='twitter_id',
            field=models.IntegerField(default=None),
            preserve_default=True,
        ),
    ]
