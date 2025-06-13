from sqlalchemy.orm import Session
from . import models, schemas
from .services.sentiment import analyze_sentiment
from .schemas import FeedbackCreate
from app.utils.nlp_utils import analyze_sentiment

def classify_sentiment(score: float) -> str:
    if score >= 0.66:
        return "positive"
    elif score <= 0.33:
        return "negative"
    else:
        return "neutral"

def create_feedback(db: Session, feedback: FeedbackCreate):
    sentiment = analyze_sentiment(feedback.raw_text)
    sentiment_label = classify_sentiment(sentiment)

    db_feedback = models.Feedback(
        channel=feedback.channel,
        raw_text=feedback.raw_text,
        user_id=feedback.user_id,
        sentiment_score=sentiment,
        sentiment_label=sentiment_label
    )
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def get_feedbacks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Feedback).offset(skip).limit(limit).all()
