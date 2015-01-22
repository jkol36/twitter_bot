from django.db import models


# Create your models here.

class TwitterStatus(models.Model):
	text = models.CharField(max_length=250)
	twitter_id = models.IntegerField(null=True, blank=True, default=None)
	author = models.ForeignKey('TwitterUser', related_name='authors', null = True, blank = True)
	hashtags = models.ManyToManyField('hashtag', related_name='statuses', blank=True, null=True)
	favorite_count = models.IntegerField(null=True, blank=True)
	retweet_count = models.IntegerField(null=True, blank=True)
	is_favorited = models.BooleanField(default=False)
	author_followed = models.BooleanField(default=False)

	def __unicode__(self):
		return unicode(self.text)

	def tweet_author(self):
		return self.author

	def favorite_count(self):
		return self.favorite_count

	def retweet_count(self):
		return self.retweet_count

	def has_favorited(self):
		return self.is_favorited

class TwitterUser(models.Model):
	twitter_id = models.IntegerField()
	screen_name = models.CharField(max_length=250)
	followers_count = models.IntegerField()
	friends_count = models.IntegerField()
	location = models.CharField(max_length=250)
	is_followed = models.BooleanField(default=False)
	unfollowed = models.BooleanField(default=False)

	def __unicode__(self):
		return self.screen_name

	def get_twitter_id(self):
		return self.twitter_id

	def get_followers_count(self):
		return self.followers_count

	def get_friends_count(self):
		return self.friends_count

	def get_location(self):
		return self.location

class OauthSet(models.Model):
	access_token = models.CharField(max_length=250)
	access_token_secret = models.CharField(max_length=250)
	consumer_key = models.CharField(max_length=250)
	consumer_secret = models.CharField(max_length=250)

	def __unicode__(self):
		return self.access_token

	def get_access_secret(self):
		return self.access_token_secret

	def get_consumer_key(self):
		return self.consumer_key

	def get_consumer_secret(self):
		return self.consumer_secret

class hashtag(models.Model):
	name = models.CharField(max_length=250)

	def __unicode__(self):
		return self.name



