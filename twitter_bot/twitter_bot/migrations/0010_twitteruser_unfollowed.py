# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_bot', '0009_twitteruser_is_followed'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteruser',
            name='unfollowed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
