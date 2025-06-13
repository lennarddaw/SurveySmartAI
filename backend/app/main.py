from fastapi import FastAPI
from .database import Base, engine
from .api.v1.routes import feedback

Base.metadata.create_all(bind=engine)

app = FastAPI(title="SurveySmart.ai API")

app.include_router(feedback.router)
