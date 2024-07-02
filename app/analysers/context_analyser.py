from textblob import TextBlob

def analyze_emotional_content(text: str) -> str:

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    
    if sentiment < -0.1:
        return "NEGAIVE"
    elif -0.1 <= sentiment <= 0.1:
        return "NEUTRAL"
    else:
        return "POSITIVE"

