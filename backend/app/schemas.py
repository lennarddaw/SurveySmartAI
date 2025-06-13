from pydantic import BaseModel, validator
from typing import Optional, List
from uuid import UUID
from datetime import datetime
import json

class FeedbackCreate(BaseModel):
    channel: str
    raw_text: str
    user_id: Optional[str] = None

class EmotionScore(BaseModel):
    label: str
    score: float

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
    keywords: Optional[List[str]] = None
    emotions: Optional[List[EmotionScore]] = None
    created_at: datetime
    updated_at: datetime

    # 🛠 Wichtig: String → List[EmotionScore] umwandeln, wenn nötig
    @validator("emotions", pre=True)
    def parse_emotions(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except json.JSONDecodeError:
                return []
        return v

    class Config:
        orm_mode = True
