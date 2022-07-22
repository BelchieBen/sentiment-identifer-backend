import re 
import math

def removeEmoji(tweet):
    tweet.encode('ascii', 'ignore').decode('ascii')
    clean_tweet = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweet)
    return clean_tweet

def categorizeSentiment(sentiment): 
    if math.isclose(sentiment, 0.5) or math.isclose(sentiment,0.4) or math.isclose(sentiment,0.3) or math.isclose(sentiment, 0.2)  :
        return "Mostly Positive"
    elif math.isclose(sentiment,1) or math.isclose(sentiment,0.9) or math.isclose(sentiment,0.8) or math.isclose(sentiment,0.7) or math.isclose(sentiment,0.6):
        return "Very Positive"
    elif math.isclose(sentiment,-0.2) or math.isclose(sentiment,-0.3) or math.isclose(sentiment,-0.4) or math.isclose(sentiment,-0.5):
        return "Mostly Negative"
    elif  math.isclose(sentiment,-0.6) or math.isclose(sentiment,-0.7) or math.isclose(sentiment,-0.8) or math.isclose(sentiment,-0.9) or math.isclose(sentiment,-1):
        return "Very Negative"
    elif math.isclose(sentiment,0.1) or math.isclose(sentiment,0) or math.isclose(sentiment,-0.1):
        return "Neutral"   
    else:
        return

def categorizeSubjectivity(subjectivity):
    if math.isclose(subjectivity,0) or math.isclose(subjectivity,0.1) or math.isclose(subjectivity,0.2):
        return "Very Objective"        
    if math.isclose(subjectivity,0.3) or math.isclose(subjectivity,0.4) or math.isclose(subjectivity,0.5):
        return "Mostly Objective"
    if math.isclose(subjectivity,0.6) or math.isclose(subjectivity,0.7) or math.isclose(subjectivity,0.8):
        return "Mostly Subjective"
    if math.isclose(subjectivity,0.8) or math.isclose(subjectivity,0.9) or math.isclose(subjectivity,1):
        return "Very Subjective"
    else:
        return

