# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_bot', '0007_auto_20150122_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitterstatus',
            name='author',
            field=models.ForeignKey(related_name='authors', blank=True, to='twitter_bot.TwitterUser', null=True),
            preserve_default=True,
        ),
    ]
