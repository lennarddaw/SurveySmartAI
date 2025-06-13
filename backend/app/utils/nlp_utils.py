from transformers import pipeline
from keybert import KeyBERT

sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
emotion_pipeline = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", top_k=3)

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

kw_model = KeyBERT()

def detect_emotion(text: str) -> str:
    try:
        result = emotion_pipeline(text)[0][0]  # top_k=1 liefert Liste mit einem Dict
        return result["label"]
    except Exception as e:
        print(f"Emotion error: {e}")
        return "unknown"

def analyze_emotions(text: str) -> list[dict]:
    try:
        results = emotion_pipeline(text)  # gibt Liste mit Liste zurück
        if isinstance(results, list) and isinstance(results[0], list):
            results = results[0]
        top_emotions = [
            {"label": r["label"].lower(), "score": round(r["score"], 2)}
            for r in results
        ]
        return top_emotions
    except Exception as e:
        print(f"Emotion analysis error: {e}")
        return []



def extract_keywords(text: str, top_n: int = 5) -> list[str]:
    try:
        keywords = kw_model.extract_keywords(text, top_n=top_n, stop_words="english")
        return [kw[0] for kw in keywords]
    except Exception as e:
        print(f"Keyword extraction error: {e}")
        return []
