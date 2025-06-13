from sqlalchemy.orm import Session
from . import models, schemas
from .services.sentiment import analyze_sentiment  # Neu

def create_feedback(db: Session, fb: schemas.FeedbackCreate):
    sentiment_score = analyze_sentiment(fb.raw_text)  # Neu
    db_fb = models.Feedback(
        channel=fb.channel,
        raw_text=fb.raw_text,
        sentiment_score=sentiment_score,  # Neu
        user_id=fb.user_id,               # Optional: falls vorhanden
        status="new"                      # Optional: Defaultwert
    )
    db.add(db_fb)
    db.commit()
    db.refresh(db_fb)
    return db_fb

def get_feedbacks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Feedback).offset(skip).limit(limit).all()
