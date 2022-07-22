import re 

def removeEmoji(tweet):
    tweet.encode('ascii', 'ignore').decode('ascii')
    clean_tweet = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet)
    return clean_tweet

def categorizeSentiment(sentiment):
    if sentiment == 0.2 or -0.1 or 0 or -0.1 or 0.2:
        return "Neutral"        
    if sentiment == 0.6 or 0.5 or 0.4 or 0.3:
        return "Mostly Positive"
    if sentiment == 1 or 0.9 or 0.8 or 0.7:
        return "Very Positive"
    if sentiment == -0.3 or -0.4 or -0.5 or -0.6:
        return "Mostly Negative"
    if sentiment == -0.7 or -0.8 or -0.9 or -1:
        return "Very Negative"
    else:
        return

def categorizeSubjectivity(subjectivity):
    if subjectivity ==  0 or 0.1 or 0.2:
        return "Very Objective"        
    if subjectivity == 0.3 or 0.4 or 0.5:
        return "Mostly Objective"
    if subjectivity == 0.6 or 0.7 or 0.8:
        return "Mostly Subjective"
    if subjectivity == 0.8 or 0.9 or 1:
        return "Very Subjective"
    else:
        return

