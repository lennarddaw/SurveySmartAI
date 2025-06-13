from sqlalchemy.orm import Session
from . import models, schemas

def create_feedback(db: Session, fb: schemas.FeedbackCreate):
    db_fb = models.Feedback(channel=fb.channel, raw_text=fb.raw_text)
    db.add(db_fb)
    db.commit()
    db.refresh(db_fb)
    return db_fb

def get_feedbacks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Feedback).offset(skip).limit(limit).all()
