from django.core.management.base import BaseCommand, CommandError
import sys
import os
import tweepy
from twitter.models import Author, Tweet

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_key = os.environ['ACCESS_KEY']
access_secret = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class Command(BaseCommand):
    args = None
    help = 'Loads some tweets'

    def handle(self, *args, **options):
        sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
        sapi.sample()


class CustomStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            #print(status
            if status.place:
                print("\t" + str(dir(status.place)))
                print("\t" + str(status.place.bounding_box))
                print("\t" + str(status.place.full_name))
                print("\t" + str(status.place.country))

            #not all have this???
            #print("\t" + str(status.possibly_sensitive))
            author, created = Author.objects.get_or_create(
                twitter_id=status.author.id,
                defaults = {
                    'statuses_count':status.author.statuses_count,
                    'followers_count':status.author.followers_count,
                    'profile_image_url':status.author.profile_image_url,
                }
            )

            tweet = Tweet.objects.create(
                author=author,
                text=status.text,
                created_at=status.created_at,
                source=status.source,
                retweet_count=int(status.retweet_count)
            )
            if status.place:
                tweet.location_name=status.place.full_name
                tweet.country=status.place.country
                tweet.save()

        except Exception as e:
            print e

    def on_error(self, status_code):
        print(sys.stderr, 'Encountered error with status code:' + status_code)
        return True

    def on_timeout(self):
        print(sys.stderr + 'Timeout...')
        return True
