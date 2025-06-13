from fastapi import FastAPI

from app.api.v1.routes import feedback

app = FastAPI()

@app.get("/")
def root():
    return {"status": "SurveySmart.AI is running"}

app.include_router(feedback.router, prefix="/api/v1/feedback")
