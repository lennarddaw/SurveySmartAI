from transformers import pipeline
from keybert import KeyBERT

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text: str) -> float:
    try:
        result = sentiment_pipeline(text)[0]
        label = result["label"].lower()
        score = result["score"]

        if "positive" in label:
            return round(score, 2)
        elif "negative" in label:
            return round(-score, 2)
        else:
            return 0.0
    except Exception as e:
        print(f"Sentiment error: {e}")
        return 0.0

# ✅ Keyword-Analyse
kw_model = KeyBERT()

def extract_keywords(text: str, top_n: int = 5) -> list[str]:
    try:
        keywords = kw_model.extract_keywords(text, top_n=top_n, stop_words="english")
        return [kw[0] for kw in keywords]
    except Exception as e:
        print(f"Keyword extraction error: {e}")
        return []
