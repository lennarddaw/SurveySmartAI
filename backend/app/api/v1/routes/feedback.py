from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....database import SessionLocal
from .... import crud, schemas

router = APIRouter(prefix="/feedback", tags=["feedback"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Feedback)
def create(fb: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    return crud.create_feedback(db, fb)

@router.get("/", response_model=list[schemas.Feedback])
def list_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_feedbacks(db, skip, limit)
