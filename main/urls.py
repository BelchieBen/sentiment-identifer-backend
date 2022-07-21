from django.urls import path
from . views import *

urlpatterns = [
    path('', GetSentiment),
    path('tweet/search', SearchForTweets)
]
