from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="oliverguhr/german-sentiment-bert")

def analyze_sentiment(text: str) -> float:
    try:
        result = sentiment_pipeline(text)[0]
        label = result["label"].lower()
        score = result["score"]

        if label == "positive":
            return round(score, 2)
        elif label == "negative":
            return round(-score, 2)
        else:
            return 0.0
    except Exception as e:
        print(f"Sentiment error: {e}")
        return 0.0
