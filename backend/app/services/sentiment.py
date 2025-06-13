from textblob import TextBlob

def analyze_sentiment(text: str) -> float:
    return round(TextBlob(text).sentiment.polarity, 3)
