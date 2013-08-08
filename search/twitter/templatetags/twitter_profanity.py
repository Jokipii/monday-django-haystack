from django import template
from django.conf import settings
import re

register = template.Library()

@register.filter(name="twitter_profanity_filter")
def twitter_profanity_filter(value):
    word_list = getattr(settings, 'PROFANITY_LIST', None)
    if word_list:
        for word in word_list:
            regex = '(?i)%s' %word.lower()
            r = re.compile(regex)
            value = r.sub('*'*len(word), value)
    return value
