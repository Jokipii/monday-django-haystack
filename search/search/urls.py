from django.conf.urls import patterns, include, url

from twitter.views import TweetList
from haystack.views import SearchView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TweetList.as_view(), name='home'),
    url(r'^search/', SearchView(load_all=False)),
    url(r'^search/', include('haystack.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
