# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_bot', '0008_auto_20150122_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitteruser',
            name='is_followed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
