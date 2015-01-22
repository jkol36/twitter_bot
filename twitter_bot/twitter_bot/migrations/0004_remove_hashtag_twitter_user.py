# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_bot', '0003_hashtag_twitter_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtag',
            name='twitter_user',
        ),
    ]
