from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import datetime

class FeedbackCreate(BaseModel):
    channel: str
    raw_text: str
    user_id: Optional[str] = None

class Feedback(BaseModel):
    id: UUID
    channel: str
    raw_text: str
    sentiment_score: Optional[float]
    status: str
    sentiment_label: Optional[str] = None
    user_id: Optional[str] = None
    word_count: Optional[int] = None
    language: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
