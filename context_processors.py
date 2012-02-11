from django.utils import simplejson as json
from django.conf import settings
from django.core.cache import cache

import twitter

def latest_tweets(request):
    tweets = cache.get( 'tweets' )
    if not tweets:
        tweets = twitter.Api().GetUserTimeline( settings.TWITTER_USER )[:2]
        cache.set( 'tweets', tweets, settings.TWITTER_TIMEOUT )

    return {"tweets": tweets}

