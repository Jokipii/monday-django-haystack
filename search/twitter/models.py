from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    twitter_id = models.BigIntegerField()
    friends_count = models.BigIntegerField(null=True)
    statuses_count = models.BigIntegerField(null=True)
    followers_count = models.BigIntegerField(null=True)
    profile_image_url = models.CharField(null=True, max_length=255)
    location = models.CharField(null=True, max_length=255)

    class Meta:
        db_table = 'author'

    def __unicode__(self):
        return '<Author %s, %s>' % (self.id, self.twitter_id)


class Tweet(models.Model):
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False,)
    source = models.CharField(max_length=1000)
    text = models.CharField(max_length=150)
    retweet_count = models.BigIntegerField(null=True, blank=True)
    author = models.OneToOneField(Author, blank=True, null=True)
    location_name = models.CharField(null=True, max_length=255)
    country = models.CharField(null=True, max_length=255)

    class Meta:
        db_table = 'twitter'

    def __unicode__(self):
        return '<Tweet %s, %s>' % (self.id, self.author)
