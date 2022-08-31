from django.urls import path
from . views import GetSentiment, SearchForTweets, FindUserRecentCharts

urlpatterns = [
    path('analyse', GetSentiment),
    path('tweet/search', SearchForTweets),
    path('find-latest-charts', FindUserRecentCharts)
]
