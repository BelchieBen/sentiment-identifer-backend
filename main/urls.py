from django.urls import path
from . views import *

urlpatterns = [
    path('analyse', GetSentiment),
    path('tweet/search', SearchForTweets)
]
