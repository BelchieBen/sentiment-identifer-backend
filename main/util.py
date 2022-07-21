import re 

def removeEmoji(tweet):
    tweet.encode('ascii', 'ignore').decode('ascii')
    clean_tweet = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet)
    return clean_tweet