from django.contrib import admin

from models import Author, Tweet


class TweetAdmin(admin.ModelAdmin):
    model = Tweet
    list_display = ('created_at', 'source','retweet_count', 'location_name', 'country',)
    fields = ('text', 'created_at', 'source','retweet_count', 'location_name', 'country',)
    search_fields = ('text', 'created_at', 'source', 'location_name', 'country',)
    list_filter = ('created_at', 'country')


admin.site.register(Author)
admin.site.register(Tweet, TweetAdmin)
