import os
import sys
from optparse import OptionParser
import time
import tweepy
import math

access_token = '258627515-2YbIS6XXingGqlumiyQQTpFNTVUFrr1dNuUN79g4'
access_token_secret = 'vFzKBe3HpfMuuZWyblAIHW0fIT0K17vKz4OIFxtpG8xS0'
consumer_key = '3Gsg8IIX95Wxq28pDEkA'
consumer_secret = 'LjEPM4kQAC0XE81bgktdHAaND3am9tTllXghn0B639o'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)



def auth_info():
	api = tweepy.API(auth)
	return api.rate_limit_status()

def get_follower_count():
	api = tweepy.API(auth)
	return api.me().followers_count

def get_following_count():
	api = tweepy.API(auth)
	return api.me().friends_count

def dir_of_auth():
	api = tweepy.API(auth)
	return dir(api)
def me():
	api = tweepy.API(auth)
	return api.me()
def get_follow_requests_left():
	api = tweepy.API(auth)
	return api.rate_limit_status()['resources']['followers']['/followers/ids']['remaining']

def get_favorites_requests_left():
	api = tweepy.API(auth)
	return api.rate_limit_status()['resources']['favorites']['/favorites/ids']['remaining']

def unfollow_nonfollowers():
	api = tweepy.API(auth)
	followers = set(api.followers_ids)
	following = set(api.friends_ids)
	unfollow = set(followers - following)
	for i in unfollow:
		try:
			api.destroy_friendship(i)
		except Exception, e:
			process_exception(e)

def process_exception(error):
	try:
		code = error.args[0]['code']
	except Exception, e:
		print e


def random_num():
	return math.randomint(0, 100)

def main():
	api = tweepy.API(auth)
	followers_count = get_follower_count()
	following_count = get_following_count()
	hashtags = hashtag.objects.filter(Q(name='entrepreneur') | Q(name='startups') | Q(name='programming') | Q(name='hacking'))
	tweets = TwitterStatus.objects.filter(hashtags=hashtags)
	following_ids = set(api.friends_ids())
	#saved in the database
	people_i_unfollowed = set(TwitterUser.objects.filter(unfollowed=True))
	#saved in the database
	Already_Favorited = set(TwitterStatus.objects.filter(is_favorited=True))
	#saved in the database
	Already_Followed = set(TwitterUser.objects.filter(is_followed=True))
	#keep track of ids i follow in this iteration
	followed = []
	#keep track of tweets i favorite during this iteration
	favorited = []
	#keep track of users I unfollow
	unfollowed = []
	Ignore = people_i_unfollowed.union(Already_Followed)
	while 1:
		if followers_count > following_count and tweets > 0:
			print 'all_good'
			for tweet in tweets:
				if tweet.twitter_id not in Already_Favorited and tweet.twitter_id:
					try:
						api.create_favorite(tweet.twitter_id)
						favorited.append(tweet.twitter_id)
					except Exception, e:
						process_e = process_exception(e)
				try:
					if tweet.author.twitter_id not in Ignore:
						api.create_friendship(tweet.author.twitter_id)
						followed.append(tweet.author.twitter_id)
				except Exception, e:
					process_e = process_exception(e)
			#write favorites to database
			try:
				for twitter_id in favorited:
					status = TwitterStatus.objects.get(twitter_id=twitter_id)
					status.is_favorited = True
					status.save()
			except Exception, e:
				process_e = process_exception(e)
			#Write followed ids to database
			try:
				for twitter_id in followed:
					user = TwitterUser.objects.get(twitter_id=twitter_id)
					user.is_followed = True
					user.save()
					time.sleep(random_num())
			except Exception, e:
				process_e = process_exception(e)
			#write unfollowed to database
			try:
				for twitter_id in unfollowed:
					user = TwitterUser.objects.get(twitter_id=twitter_id)
					user.unfollowed = True
					user.save()
			except Exception, e:
				process_e = process_exception(e)
		#if I have more followers than I'm following, but there aren't any tweets.
		elif followers_count > following_count and tweets < 0:
			#sleep and then get more tweets
			time.sleep(30)
			tweets = TwitterStatus.objects.filter(hashtags=hashtags)
		elif followers_count < following_count:
			action = unfollow_nonfollowers()
			time.sleep(200)

if __name__ == '__main__':
	usage = 'usage: %prog -s PATH | --path==PATH'
	parser = OptionParser(usage)
	parser.add_option('-s', '--path', dest='path', metavar='PATH', help='The Path to the django environmnet')
	(options, args) = parser.parse_args()
	if not options.path:
		parser.error("Specify the path where manage.py is")
 
	os.environ['DJANGO_SETTINGS_MODULE'] = "twitter_bot.settings"
	sys.path.append(options.path)

	###################IMPORTS ######################
	from twitter_bot.twitter_bot.models import hashtag, TwitterUser, TwitterStatus
	from django.core.wsgi import get_wsgi_application
	application = get_wsgi_application()
	from django.db.models import Q

	main()



