import sqlalchemy as sa
from .database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Column, String, Text, DateTime, Integer
from sqlalchemy.dialects.postgresql import ARRAY

class Feedback(Base):
    __tablename__ = "feedback"
    id = sa.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    channel = sa.Column(sa.String(32), nullable=False)
    raw_text = sa.Column(sa.Text, nullable=False)
    sentiment_score = sa.Column(sa.Numeric(3, 2), nullable=True)
    status = sa.Column(sa.String(16), nullable=False, default="new")
    word_count = Column(Integer, nullable=True)
    language = Column(String, nullable=True)
    keywords = Column(ARRAY(String), nullable=True)
    user_id = Column(String, nullable=True)
    created_at = sa.Column(sa.TIMESTAMP(timezone=True), server_default=sa.func.now())
    updated_at = sa.Column(sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), onupdate=sa.func.now())
    sentiment_label = Column(String, nullable=True)

