# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hashtag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OauthSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('access_token', models.CharField(max_length=250)),
                ('access_token_secret', models.CharField(max_length=250)),
                ('consumer_key', models.CharField(max_length=250)),
                ('consumer_secret', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TwitterStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('is_favorited', models.BooleanField(default=False)),
                ('author_followed', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter_id', models.IntegerField()),
                ('screen_name', models.CharField(max_length=250)),
                ('followers_count', models.IntegerField()),
                ('friends_count', models.IntegerField()),
                ('location', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
