from django.urls import path
from . views import GetSentiment, SearchForTweets

urlpatterns = [
    path('analyse', GetSentiment),
    path('tweet/search', SearchForTweets),
]
