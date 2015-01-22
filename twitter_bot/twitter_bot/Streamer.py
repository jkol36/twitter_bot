import os
import sys
import tweepy
from optparse import OptionParser
import time

class Streamer(tweepy.StreamListener):
	def __init__(self, *args, **kwargs):
		self.hashtags = kwargs.pop('hashtags')
		self.checker = time.time()
		return super(Streamer, self).__init__(*args, **kwargs)

	def on_status(self, status):
		self.process_status(status)
		return self.should_continue()

	def on_error(self, error):
		print error
		return self.should_continue()

	def on_timeout(self):
		print 'timed out'
		return self.should_continue()

	def should_continue(self):
		if time.time() - self.checker > 128:
			self.checker = time.time()
			return set(hashtag.objects.all()) == set(self.hashtags)
		return True

	def is_good(self, user):
		if user.default_profile_image:
			return False
		if not user.description or 'bot' in user.description:
			return False
		if user.followers_count < 50:
			return False
		if int(user.friends_count) / float(user.followers_count) > 3:
			return False

		if not user.name:
			return False
		return True

	def process_status(self, status):
		user, _ = TwitterUser.objects.get_or_create(twitter_id=status.user.id, screen_name = status.user.screen_name.encode('utf-8'), followers_count= status.user.followers_count, friends_count=status.user.friends_count, location=status.user.location.encode('utf-8'))
		user.save()
		mstatus = TwitterStatus()
		mstatus.twitter_id = status.id
		mstatus.author = user
		mstatus.text = status.text.encode('utf-8')
		mstatus.favorite_count = status.favorite_count
		mstatus.retweet_count = status.retweet_count
		mstatus.save()
		for d in status.entities['hashtags']:
			h, _ = hashtag.objects.get_or_create(name=d['text'].lstrip('#').lower())
			mstatus.hashtags.add(h)
			h.save()

class Worker:
		def __init__(self):
			apikey = 'moX6M9jbbIuAnYuaAxZJFkzQY'
			apisecret = 'YhH1Fgr4VUyzLsKoKKQrR0bRuPbsqP4daiiZ9UbbSyZWDCsTxU'
			access_token = '1177046514-QVUDUBANp0p2HHiJrBJIwYXyaqjZkQg7NMHSRwA'
			access_secret = 'gBDQ3Z2wNGMOptyAsLffOHksIbhYlL6RvbCYSHzkWV08s'
			self.auth = tweepy.OAuthHandler(apikey, apisecret)
			self.auth.set_access_token(access_token, access_secret)

		def stream(self):
			while 1:
				hashtags = hashtag.objects.filter()[:50]
				print hashtags
				if not hashtags:
					print 'no hashtags'
					time.sleep(10)
				try:
					stream = tweepy.Stream(self.auth, Streamer(hashtags=hashtags))
				except Exception, e:
					print e
					print 'Error on stream. Now Sleeping'
					time.sleep(20)
				try:
					stream.filter(track=['#'+h.name for h in hashtags], languages=['en'])
				except Exception, e:
					print e
					print 'error on stream.filter now sleeping'
					time.sleep(20)

if __name__ == '__main__':
	usage = 'usage: %pprog -s PATH | --path=PATH'
	parser = OptionParser(usage)
	parser.add_option('-s', '--path', dest='path', metavar='PATH', help="The path to the Django environment")
	(options, args) = parser.parse_args()
	
	if not options.path:
		parser.error("Specify the path where manage.py is")
 
	os.environ['DJANGO_SETTINGS_MODULE'] = "twitter_bot.settings"
	sys.path.append(options.path)

	#####################IMPORTS###################
	from twitter_bot.twitter_bot.models import hashtag, TwitterUser, TwitterStatus
	from django.core.wsgi import get_wsgi_application
	application = get_wsgi_application()

	a = Worker()
	a.stream()






