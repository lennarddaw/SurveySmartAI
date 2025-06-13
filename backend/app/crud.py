from sqlalchemy.orm import Session
from . import models, schemas
from .services.sentiment import analyze_sentiment
from .schemas import FeedbackCreate
from app.utils.nlp_utils import analyze_sentiment
from langdetect import detect
from sklearn.feature_extraction.text import CountVectorizer
import re
from app.utils.nlp_utils import detect_emotion

def classify_sentiment(score: float) -> str:
    if score >= 0.66:
        return "positive"
    elif score <= 0.33:
        return "negative"
    else:
        return "neutral"

def extract_keywords(text: str, top_n: int = 5) -> list[str]:
    text = re.sub(r'[^\w\s]', '', text.lower())
    vectorizer = CountVectorizer(stop_words='english', max_features=top_n)
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out().tolist()

def create_feedback(db: Session, feedback: FeedbackCreate):
    sentiment = analyze_sentiment(feedback.raw_text)
    sentiment_label = classify_sentiment(sentiment)
    word_count = len(feedback.raw_text.split())
    language = detect(feedback.raw_text)
    keywords = extract_keywords(feedback.raw_text)
    emotions = detect_emotion(feedback.raw_text)

    db_feedback = models.Feedback(
        channel=feedback.channel,
        raw_text=feedback.raw_text,
        user_id=feedback.user_id,
        sentiment_score=sentiment,
        sentiment_label=sentiment_label,
        word_count=word_count,
        language=language,
        keywords=keywords,
        emotions=emotions,
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def get_feedbacks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Feedback).offset(skip).limit(limit).all()
