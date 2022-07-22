from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import tweepy
from tweepy import OAuthHandler
from tweepy import API
import json
from . util import *

#Imports for sentiment analysis
from textblob import TextBlob

@api_view(['POST'])
def GetSentiment(request):
    #try:
        data_to_analyse = request.data

        for i in data_to_analyse["data"]:
            textToAnalyse = i["text"]
            sentiment = round(TextBlob(textToAnalyse).sentiment.polarity, 1)
            subjectivity = round(TextBlob(textToAnalyse).subjectivity, 1)
            i["sentiment"] = sentiment
            i["subjectivity"] = subjectivity
            i['sentiment_label'] = categorizeSentiment(sentiment)
            i['subjectivity_label'] = categorizeSubjectivity(subjectivity)
        return Response(data_to_analyse)
    # except:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def SearchForTweets(request):
    try:
        #Setting the API keys to let me access the twitter API
        consumer_key = '5LblTsyMGt6NEUYY69ITQOEdT'
        consumer_secret = 'gvHxYjmgN3qMF6We76PXXqhym1RVMRSXabV2Gc1ywvC9zb0J1z'
        access_token = '1346737125782335488-9cD5yLseu9W5OAde9BSDdvm4gQ4RlG'
        access_token_secret = 'iXUfotj6MxCOvtowC0ao7Z1maqLG025TWCVuSowgZc34J'

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        searchWord = request.data['keyword']
        numberOfTweets = int(request.data['numberOfTweets'])

        tweet_data = []

        for tweet in tweepy.Cursor(api.search, q=searchWord+' -filter:retweets',lang="en", tweet_mode='extended').items(numberOfTweets):
            full_text_tweet = tweet.full_text
            clean_tweet= removeEmoji(full_text_tweet)
            convert_tweet = {"text":clean_tweet, "posted_at":tweet.created_at, "id":tweet.id}
            tweet_data.append(convert_tweet)
        return Response(tweet_data)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    
