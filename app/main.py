from fastapi import FastAPI
from pydantic import BaseModel

import sys
from pathlib import Path

# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "src"))

from predict import predict_news

app = FastAPI(title="Fake News Detection API")


class NewsRequest(BaseModel):
    news: str


@app.get("/")
def home():
    return {
        "message": "Fake News Detection API is running!"
    }


@app.post("/predict")
def predict(request: NewsRequest):

    prediction = predict_news(request.news)

    return {
        "prediction": prediction
    }