# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitter_bot', '0006_auto_20150122_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitterstatus',
            name='twitter_id',
            field=models.IntegerField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
